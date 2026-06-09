#!/usr/bin/env node

import { execFileSync } from "node:child_process";
import { access, readFile, readdir, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = path.resolve(import.meta.dirname, "..");
const network = process.argv.includes("--network");
const failures = [];
const warnings = [];

function fail(scope, message) {
  failures.push(`${scope}: ${message}`);
}

function warn(scope, message) {
  warnings.push(`${scope}: ${message}`);
}

function verifyNoGeneratedArtifactDiff() {
  if (process.env.ALLOW_GENERATED_ARTIFACT_DIFF === "1") {
    return;
  }

  try {
    const artifactPathspecs = [
      "*.pdf",
      "*.pptx",
      "llm-rl-algorithms-2026/assets/formulas/*",
    ];
    const diffArgs = ["diff", "--name-only", "--", ...artifactPathspecs];
    const cachedDiffArgs = [
      "diff",
      "--cached",
      "--name-only",
      "--",
      ...artifactPathspecs,
    ];
    const changed = unique(
      [
        execFileSync("git", diffArgs, { cwd: root, encoding: "utf8" }),
        execFileSync("git", cachedDiffArgs, { cwd: root, encoding: "utf8" }),
      ]
        .join("\n")
        .split(/\r?\n/)
        .filter(Boolean),
    );

    if (changed.length > 0) {
      fail(
        "generated artifacts",
        "uncommitted PDF/PPTX/formula diffs are blocked; set " +
          "ALLOW_GENERATED_ARTIFACT_DIFF=1 only after font and render review: " +
          changed.join(", "),
      );
    }
  } catch (error) {
    warn("generated artifacts", `could not inspect git diff: ${error.message}`);
  }
}

async function exists(file) {
  try {
    await access(file);
    return true;
  } catch {
    return false;
  }
}

function unique(values) {
  return [...new Set(values)];
}

function extractUrls(text) {
  return unique(
    [...text.matchAll(/https?:\/\/[^\s)\]>"']+/g)]
      .map((match) => match[0].replace(/[`.,;:]+$/, "")),
  );
}

function extractCitationIds(text) {
  return unique(
    [...text.matchAll(/\b([SR]\d{1,3})\b/g)].map((match) => match[1]),
  );
}

function parseDelimitedLine(line, delimiter) {
  const cells = [];
  let cell = "";
  let quoted = false;

  for (let index = 0; index < line.length; index += 1) {
    const char = line[index];
    if (char === '"') {
      if (quoted && line[index + 1] === '"') {
        cell += '"';
        index += 1;
      } else {
        quoted = !quoted;
      }
    } else if (char === delimiter && !quoted) {
      cells.push(cell);
      cell = "";
    } else {
      cell += char;
    }
  }
  cells.push(cell);
  return cells;
}

async function verifyDelimitedFile(file) {
  const text = await readFile(file, "utf8");
  const lines = text.split(/\r?\n/).filter((line) => line.length > 0);
  if (lines.length === 0) {
    fail(path.relative(root, file), "empty structured data file");
    return;
  }

  const delimiter = file.endsWith(".tsv") ? "\t" : ",";
  const expected = parseDelimitedLine(lines[0], delimiter).length;
  for (let index = 1; index < lines.length; index += 1) {
    const count = parseDelimitedLine(lines[index], delimiter).length;
    if (count !== expected) {
      fail(
        path.relative(root, file),
        `row ${index + 1} has ${count} columns; expected ${expected}`,
      );
    }
  }
}

function verifyPdf(file, slug) {
  try {
    const info = execFileSync("pdfinfo", [file], { encoding: "utf8" });
    const pages = Number(info.match(/^Pages:\s+(\d+)/m)?.[1] ?? 0);
    if (pages < 1) {
      fail(slug, "PDF has no pages");
    }

    const text = execFileSync("pdftotext", [file, "-"], {
      encoding: "utf8",
      maxBuffer: 64 * 1024 * 1024,
    });
    if (text.replace(/\s/g, "").length < 500) {
      fail(slug, "PDF text extraction is unexpectedly short");
    }
    if (/\b(?:TODO|TBD)\b|Lorem ipsum/i.test(text)) {
      fail(slug, "PDF contains placeholder text");
    }
  } catch (error) {
    fail(slug, `PDF verification failed: ${error.message}`);
  }
}

async function checkUrl(url) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 15_000);
  try {
    const response = await fetch(url, {
      redirect: "follow",
      headers: {
        Range: "bytes=0-2047",
        "User-Agent": "manuscripts-repository-verifier/1.0",
      },
      signal: controller.signal,
    });
    return response.status;
  } catch (error) {
    return `${error.name}: ${error.message}`;
  } finally {
    clearTimeout(timeout);
  }
}

async function runNetworkChecks(urlOwners) {
  const urls = [...urlOwners.keys()];
  let cursor = 0;

  async function worker() {
    while (cursor < urls.length) {
      const url = urls[cursor];
      cursor += 1;
      const result = await checkUrl(url);
      const owners = [...urlOwners.get(url)].join(", ");

      if (result === 404 || result === 410) {
        fail(owners, `dead source URL (${result}): ${url}`);
      } else if (typeof result === "string" || result >= 400) {
        warn(owners, `source URL needs manual review (${result}): ${url}`);
      }
    }
  }

  await Promise.all(Array.from({ length: 16 }, worker));
}

const entries = await readdir(root, { withFileTypes: true });
const works = [];
for (const entry of entries) {
  if (!entry.isDirectory() || entry.name.startsWith(".")) {
    continue;
  }
  if (await exists(path.join(root, entry.name, "index.html"))) {
    works.push(entry.name);
  }
}
works.sort();

if (works.length === 0) {
  fail("repository", "no work directories found");
}

verifyNoGeneratedArtifactDiff();

const catalogue = await readFile(path.join(root, "README.md"), "utf8");
const urlOwners = new Map();

for (const slug of works) {
  const directory = path.join(root, slug);
  const required = [
    "README.md",
    "sources.md",
    "index.html",
    `${slug}.pdf`,
  ];

  for (const name of required) {
    if (!(await exists(path.join(directory, name)))) {
      fail(slug, `missing ${name}`);
    }
  }

  if (!catalogue.includes(`${slug}/index.html`)) {
    fail("README.md", `catalogue does not list ${slug}`);
  }

  const html = await readFile(path.join(directory, "index.html"), "utf8");
  const sources = await readFile(path.join(directory, "sources.md"), "utf8");
  const title = html.match(/<title>([\s\S]*?)<\/title>/i)?.[1]?.trim();
  if (!title) {
    fail(slug, "HTML title is missing");
  }

  if (
    /(?<!\$)\{\{\s*[A-Za-z_]|\b(?:TODO|TBD)\b|Lorem ipsum/i.test(html)
  ) {
    fail(slug, "HTML contains unresolved template or placeholder text");
  }
  if (/file:\/\/|\/Users\/|\/private\/tmp\//.test(html)) {
    fail(slug, "HTML contains a machine-local path");
  }

  const localRefs = [
    ...html.matchAll(/(?:src|href)=["']([^"'#]+)["']/gi),
  ]
    .map((match) => match[1])
    .filter(
      (ref) =>
        !/^(?:https?:|mailto:|data:|javascript:|\/)/i.test(ref),
    );
  for (const ref of unique(localRefs)) {
    const clean = decodeURIComponent(ref.split("?")[0]);
    if (!(await exists(path.resolve(directory, clean)))) {
      fail(slug, `missing local HTML resource: ${ref}`);
    }
  }

  let evidence = sources;
  const dataDirectory = path.join(directory, "data");
  if (await exists(dataDirectory)) {
    const dataFiles = await readdir(dataDirectory);
    for (const name of dataFiles) {
      const file = path.join(dataDirectory, name);
      const fileStat = await stat(file);
      if (!fileStat.isFile()) {
        continue;
      }
      if (/\.(?:csv|tsv)$/i.test(name)) {
        await verifyDelimitedFile(file);
      }
      if (/(?:source|claim)-map.*\.(?:csv|tsv)$/i.test(name)) {
        evidence += `\n${await readFile(file, "utf8")}`;
      }
    }
  }

  const cited = extractCitationIds(html);
  const defined = extractCitationIds(evidence);
  for (const citation of cited) {
    if (!defined.includes(citation)) {
      fail(slug, `citation ${citation} has no source definition`);
    }
  }

  const urls = extractUrls(evidence);
  if (urls.length === 0) {
    fail(slug, "sources contain no external URLs");
  }
  for (const url of urls) {
    if (url.endsWith("`")) {
      fail(slug, `malformed source URL: ${url}`);
    }
    if (!urlOwners.has(url)) {
      urlOwners.set(url, new Set());
    }
    urlOwners.get(url).add(slug);
  }

  const pdf = path.join(directory, `${slug}.pdf`);
  if (await exists(pdf)) {
    const pdfStat = await stat(pdf);
    if (pdfStat.size < 10_000) {
      fail(slug, "PDF is unexpectedly small");
    } else {
      verifyPdf(pdf, slug);
    }
  }
}

if (network) {
  await runNetworkChecks(urlOwners);
}

for (const message of warnings) {
  console.warn(`WARN ${message}`);
}
for (const message of failures) {
  console.error(`FAIL ${message}`);
}

console.log(
  `Checked ${works.length} works, ${urlOwners.size} source URLs, ` +
    `${warnings.length} warnings, ${failures.length} failures.`,
);

process.exit(failures.length === 0 ? 0 : 1);
