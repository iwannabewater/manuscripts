#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(new URL("..", import.meta.url).pathname);
const urlPattern = /https?:\/\/[^\s<>)"'`]+/g;
const urls = new Map();
const concurrency = Number.parseInt(process.env.NETWORK_CONCURRENCY || "32", 10);
const timeoutMs = Number.parseInt(process.env.NETWORK_TIMEOUT_MS || "12000", 10);
const progressEvery = Number.parseInt(process.env.NETWORK_PROGRESS_EVERY || "100", 10);
const ignoredUrlPatterns = [
  /^https?:\/\/USERNAME\.github\.io(?:\/|$)/i,
  /^https?:\/\/(?:www\.)?example\.com(?:\/|$)/i,
  /^https?:\/\/vault\.example\.com(?:\/|$)/i,
  /^http:\/\/service\//i,
];

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(path.join(root, dir), { withFileTypes: true })) {
    const rel = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if ([".git", ".venv", "node_modules", "assets"].includes(entry.name)) continue;
      walk(rel, out);
    } else {
      out.push(rel);
    }
  }
  return out;
}

function shouldCheckFile(name) {
  const normalized = name.replaceAll(path.sep, "/");
  if (!/\.(md|html|tsv|csv)$/i.test(normalized)) return false;
  if (normalized.includes("/sources/") || normalized.includes("/research/")) return false;
  return true;
}

for (const file of walk(".").filter(shouldCheckFile)) {
  const text = fs.readFileSync(path.join(root, file), "utf8");
  for (const match of text.matchAll(urlPattern)) {
    const url = match[0].replace(/[.,;:\]]+$/, "");
    if (ignoredUrlPatterns.some((pattern) => pattern.test(url))) continue;
    if (!urls.has(url)) urls.set(url, new Set());
    urls.get(url).add(file);
  }
}

const failures = [];
const manual = [];

async function probe(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  const options = {
    redirect: "follow",
    signal: controller.signal,
    headers: { "user-agent": "manuscripts-source-verifier/1.0" },
  };
  try {
    let response = await fetch(url, { ...options, method: "HEAD" });
    if (response.status >= 400) {
      response = await fetch(url, { ...options, method: "GET" });
    }
    return response.status;
  } catch (err) {
    manual.push(`${url} :: ${err.name || "error"} :: ${[...urls.get(url)].slice(0, 3).join(", ")}`);
    return null;
  } finally {
    clearTimeout(timer);
  }
}

const entries = [...urls.keys()].sort();
console.error(`checking ${entries.length} source URLs; concurrency=${concurrency}; timeout=${timeoutMs}ms`);
for (let i = 0; i < entries.length; i += concurrency) {
  const batch = entries.slice(i, i + concurrency);
  const statuses = await Promise.all(batch.map((url) => probe(url)));
  statuses.forEach((status, index) => {
    const url = batch[index];
    const files = [...urls.get(url)].slice(0, 3).join(", ");
    if (status === 404 || status === 410) failures.push(`${status} ${url} :: ${files}`);
    else if (status && status >= 400) manual.push(`${status} ${url} :: ${files}`);
  });
  const checked = Math.min(i + concurrency, entries.length);
  if (progressEvery > 0 && (checked % progressEvery < concurrency || checked === entries.length)) {
    console.error(`checked ${checked}/${entries.length}`);
  }
}

for (const item of manual) console.warn(`REVIEW ${item}`);
if (failures.length) {
  failures.forEach((item) => console.error(`FAIL ${item}`));
  process.exit(1);
}

console.log(`OK: checked ${entries.length} source URLs; ${manual.length} require manual review`);
