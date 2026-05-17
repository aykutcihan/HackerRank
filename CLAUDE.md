# CLAUDE.md — HackerRank Practice

## Project Overview

Structured HackerRank practice in **Python**, **Java**, and **TypeScript**.
Read `WORKFLOW.md` before starting any problem — it defines the full workflow and all templates.

---

## Running Code

### Java — warmup files

```bash
npm run run:java problems/001-simple-array-sum/warmups/warmup_01_read_integer.java
```

### Java — solution files (use OUTPUT_PATH internally)

```bash
echo "6\n1 2 3 4 5 6" | npm run run:java problems/001-simple-array-sum/Solution.java
```

`OUTPUT_PATH` is set automatically. File output is printed to stdout after the run.
The script also handles the `solution.java` → `Solution.java` filename mismatch automatically.

### Python

```bash
python problems/001-simple-array-sum/solution.py
```

### TypeScript

```bash
npm run run:ts problems/001-simple-array-sum/solution.ts
```

---

## Java Naming & Package Rules

- **Solution files**: named `Solution.java`, public class `Solution`, no package declaration
- **Warmup files**: named `warmup_NN_topic.java`, public class matches filename, must have `package warmups;` at the top
- Each problem folder is its own **IntelliJ module** (`NNN-problem-name.iml`) for full isolation — no class name conflicts across problems

---

## Adding a New Problem

When creating a new problem folder, also:
1. Create `NNN-problem-name.iml` inside the problem folder (see template in `WORKFLOW.md`)
2. Register the module in `.idea/modules.xml`

---

## Project Structure

```
problems/
  NNN-problem-name/
    NNN-problem-name.iml  ← IntelliJ module (one per problem)
    PROBLEM.md            ← exact problem text, read-only
    hints.md
    notes.md
    Solution.java         ← no package declaration
    solution.py
    solution.ts
    warmups/
      warmup_NN_topic.java  ← package warmups;
      warmup_NN_topic.py
      warmup_NN_topic.ts
archive/java-old/     ← 2023 solutions, reference only
scripts/
  run-java.js         ← Java compile+run helper (handles packages + OUTPUT_PATH)
out/                  ← IntelliJ compile output, gitignored
```

---

## Key Rules

- Follow `WORKFLOW.md` strictly for problem setup and the warmup ladder
- `PROBLEM.md` is read-only after creation
- JDK 17 (Temurin) is installed — `javac` and `java` are on PATH
- All communication and file content in English
