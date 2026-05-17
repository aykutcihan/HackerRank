#!/usr/bin/env node
// Compiles and runs a single Java file in isolation.
// Handles:
//   - solution.java → public class Solution  (filename/classname mismatch)
//   - package warmups; declarations          (recreates directory structure in temp dir)
//   - OUTPUT_PATH env var for HackerRank solution templates

const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: npm run run:java <path/to/File.java>');
  console.error('  e.g. npm run run:java problems/001-simple-array-sum/warmups/warmup_01_read_integer.java');
  process.exit(1);
}

const absolutePath = path.resolve(filePath);
if (!fs.existsSync(absolutePath)) {
  console.error(`File not found: ${absolutePath}`);
  process.exit(1);
}

const source = fs.readFileSync(absolutePath, 'utf8');

// Extract package (e.g. "package warmups;" → "warmups")
const packageMatch = source.match(/^\s*package\s+([\w.]+)\s*;/m);
const packageName = packageMatch ? packageMatch[1] : null;

// Extract public class name; fall back to file stem
const classMatch = source.match(/public\s+class\s+(\w+)/);
const className = classMatch ? classMatch[1] : path.basename(absolutePath, '.java');

// Fully-qualified class name for java launcher
const fullClassName = packageName ? `${packageName}.${className}` : className;

// Build temp source tree that mirrors the package structure
const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'hackerrank-'));
const packageDir = packageName
  ? path.join(tmpDir, ...packageName.split('.'))
  : tmpDir;
fs.mkdirSync(packageDir, { recursive: true });

const tmpSource = path.join(packageDir, `${className}.java`);
fs.copyFileSync(absolutePath, tmpSource);

// Compile — sourcepath lets javac resolve inter-package refs if ever needed
const compileResult = spawnSync('javac', ['-sourcepath', tmpDir, tmpSource], {
  stdio: 'inherit',
  cwd: tmpDir,
});
if (compileResult.status !== 0) {
  fs.rmSync(tmpDir, { recursive: true, force: true });
  process.exit(compileResult.status ?? 1);
}

// OUTPUT_PATH is required by HackerRank solution templates
const tmpOutput = path.join(os.tmpdir(), `hackerrank_out_${process.pid}.txt`);
if (fs.existsSync(tmpOutput)) fs.unlinkSync(tmpOutput);

const runResult = spawnSync('java', ['-cp', tmpDir, fullClassName], {
  stdio: 'inherit',
  env: { ...process.env, OUTPUT_PATH: tmpOutput },
});

// Print file output (solution files write here instead of stdout)
if (fs.existsSync(tmpOutput)) {
  const out = fs.readFileSync(tmpOutput, 'utf8');
  if (out.trim()) {
    console.log('\n--- Output (from OUTPUT_PATH) ---');
    process.stdout.write(out);
  }
  fs.unlinkSync(tmpOutput);
}

fs.rmSync(tmpDir, { recursive: true, force: true });
process.exit(runResult.status ?? 0);
