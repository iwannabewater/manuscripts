#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import path from "node:path";

const script = path.resolve(new URL(".", import.meta.url).pathname, "verify_repo.mjs");
const result = spawnSync(process.execPath, [script], { stdio: "inherit" });
process.exit(result.status ?? 1);
