#!/usr/bin/env node
import { execFileSync, spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(new URL("..", import.meta.url).pathname);
const errors = [];
const warnings = [];

const exists = (p) => fs.existsSync(path.join(root, p));
const read = (p) => fs.readFileSync(path.join(root, p), "utf8");

function addError(message) {
  errors.push(message);
}

function addWarning(message) {
  warnings.push(message);
}

function listWorkDirs() {
  return fs
    .readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => {
      if (name.startsWith(".")) return false;
      if (["assets", "scripts", "sources", "research"].includes(name)) return false;
      return exists(path.join(name, "index.html"));
    })
    .sort();
}

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(path.join(root, dir), { withFileTypes: true })) {
    const rel = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if ([".git", ".venv", "node_modules"].includes(entry.name)) continue;
      walk(rel, out);
    } else {
      out.push(rel);
    }
  }
  return out;
}

function checkDirectoryContract(workDirs) {
  const catalogue = read("README.md");
  for (const dir of workDirs) {
    for (const file of ["README.md", "index.html", "sources.md", `${dir}.pdf`]) {
      if (!exists(path.join(dir, file))) addError(`${dir}: missing ${file}`);
    }
    if (!catalogue.includes(`${dir}/index.html`)) addError(`README.md: missing ${dir}/index.html`);
    if (!catalogue.includes(`${dir}/${dir}.pdf`)) addError(`README.md: missing ${dir}/${dir}.pdf`);
  }
}

function checkLocalOnlyFiles() {
  let tracked = "";
  try {
    tracked = execFileSync("git", ["ls-files"], { cwd: root, encoding: "utf8" });
  } catch {
    addWarning("git ls-files unavailable; skipped tracked-file hygiene check");
    return;
  }
  const forbidden = [
    /^AGENTS\.md$/i,
    /^CLAUDE\.md$/i,
    /^GEMINI\.md$/i,
    /(^|\/)(QUALITY_AUDIT|HEALTH_REPORT|HUNT_REPORT|REVIEW_NOTES|WORKLOG)\.md$/i,
    /(^|\/)(audit|review|scratch|outputs)\//i,
  ];
  for (const file of tracked.trim().split(/\n/).filter(Boolean)) {
    if (forbidden.some((re) => re.test(file))) {
      addError(`local-only file is tracked: ${file}`);
    }
  }
}

function checkFontSources() {
  const files = walk(".").filter((file) => /\.(html|css|py|md)$/i.test(file));
  const sourceFiles = files.filter((file) => !file.includes("/sources/") && !file.includes("/research/"));
  const forbidden = [
    /url\(["']?fonts\/TsangerJinKai02-/,
    /url\(["']?fonts\/JetBrainsMono\.woff2/,
    /url\(["']?\.\.\/fonts\/(?:TsangerJinKai02-|JetBrainsMono\.woff2)/,
    /style\.replace\(["']\.\.\/fonts\/["'],\s*["']fonts\/["']\)/,
    /Hiragino|PingFang|Songti|STSong|Helvetica|Times-Roman|Courier|Arial|Verdana|Georgia|Source Han Serif|Noto Serif|Noto Sans|Consolas|SF Mono|Andale|Liberation Mono/,
    /font-family\s*=\s*["'][^"']*(?:,\s*|\s)(?:serif|sans-serif|monospace)\b/i,
    /font-family\s*:\s*[^;\n{}]*(?:,\s*|\s)(?:serif|sans-serif|monospace)\b/i,
  ];
  for (const file of sourceFiles) {
    const text = read(file);
    const checks = file === "assets/styles/publication-fonts.css"
      ? forbidden.filter((re) => !String(re).includes("\\.\\.\\/fonts"))
      : forbidden;
    if (checks.some((re) => re.test(text))) {
      addError(`${file}: contains forbidden or non-shared font reference`);
    }
    if (file.endsWith("index.html") && !text.includes("../assets/styles/publication-fonts.css")) {
      addError(`${file}: missing shared publication font stylesheet`);
    }
  }
  for (const dir of fs.readdirSync(root, { withFileTypes: true })) {
    if (dir.isDirectory() && dir.name !== "assets" && exists(path.join(dir.name, "fonts"))) {
      addError(`${dir.name}/fonts: per-work font directory is not allowed`);
    }
  }
  for (const name of ["TsangerJinKai02-W04.ttf", "TsangerJinKai02-W05.ttf", "JetBrainsMono.woff2"]) {
    if (!exists(path.join("assets/fonts", name))) {
      addError(`assets/fonts/${name}: missing; run make fonts`);
    }
  }
}

function splitDelimited(line, delimiter) {
  const result = [];
  let current = "";
  let inQuotes = false;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (ch === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i += 1;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (ch === delimiter && !inQuotes) {
      result.push(current);
      current = "";
    } else {
      current += ch;
    }
  }
  result.push(current);
  return result;
}

function checkDataFiles() {
  const dataFiles = walk(".").filter((file) => /\.(csv|tsv|json)$/i.test(file));
  for (const file of dataFiles) {
    const full = path.join(root, file);
    if (file.endsWith(".json")) {
      try {
        JSON.parse(fs.readFileSync(full, "utf8"));
      } catch (err) {
        addError(`${file}: invalid JSON (${err.message})`);
      }
      continue;
    }
    const delimiter = file.endsWith(".tsv") ? "\t" : ",";
    const lines = fs.readFileSync(full, "utf8").replace(/\r\n/g, "\n").split("\n").filter((line) => line.trim());
    if (lines.length === 0) {
      addError(`${file}: empty data file`);
      continue;
    }
    const header = splitDelimited(lines[0], delimiter);
    if (header.some((cell) => !cell.trim())) addError(`${file}: blank header cell`);
    for (let i = 1; i < lines.length; i += 1) {
      const cols = splitDelimited(lines[i], delimiter);
      if (cols.length !== header.length) {
        addError(`${file}:${i + 1}: expected ${header.length} columns, found ${cols.length}`);
      }
    }
  }
}

function checkPdf(pdf) {
  const info = spawnSync("pdfinfo", [pdf], { cwd: root, encoding: "utf8" });
  if (info.status !== 0) {
    addError(`${pdf}: pdfinfo failed`);
    return;
  }
  const text = spawnSync("pdftotext", [pdf, "-"], { cwd: root, encoding: "utf8", maxBuffer: 20 * 1024 * 1024 });
  if (text.status !== 0 || text.stdout.trim().length < 200) {
    addError(`${pdf}: pdftotext failed or extracted too little text`);
  }
  const fonts = spawnSync("pdffonts", [pdf], { cwd: root, encoding: "utf8" });
  if (fonts.status !== 0) {
    addError(`${pdf}: pdffonts failed`);
    return;
  }
  const lines = fonts.stdout.split("\n").slice(2).filter((line) => line.trim());
  if (!lines.some((line) => /Tsanger/i.test(line))) {
    addError(`${pdf}: no embedded Tsanger font detected`);
  }
  for (const line of lines) {
    const tail = line.match(/\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$/);
    const embedded = tail?.[1];
    if (embedded !== "yes") addError(`${pdf}: non-embedded font: ${line.trim()}`);
    const fontName = line.trim().split(/\s+/)[0].replace(/^[A-Z]{6}\+/, "");
    if (!/(Tsanger|JetBrains)/i.test(fontName)) {
      addError(`${pdf}: unapproved embedded font: ${fontName}`);
    }
  }
}

function checkPdfs(workDirs) {
  for (const dir of workDirs) {
    const pdf = path.join(dir, `${dir}.pdf`);
    if (exists(pdf)) checkPdf(pdf);
  }
}

const workDirs = listWorkDirs();
checkDirectoryContract(workDirs);
checkLocalOnlyFiles();
checkFontSources();
checkDataFiles();
checkPdfs(workDirs);

for (const warning of warnings) console.warn(`WARN ${warning}`);
if (errors.length) {
  for (const error of errors) console.error(`FAIL ${error}`);
  process.exit(1);
}

console.log(`OK: ${workDirs.length} works verified`);
