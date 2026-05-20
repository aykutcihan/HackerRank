# HackerRank Practice

A structured repository for solving HackerRank problems in **Python**, **Java**, and **TypeScript**.

## 📁 Repository Structure

```
HackerRank/
├── archive/
│   └── java-old/        # Old solutions from 2023, kept for reference
└── problems/
    └── 001-problem-name/
        ├── README.md        # Problem description, link, and notes
        ├── warmups/         # Building-block exercises before the main solution
        │   ├── warmup_01.py
        │   ├── warmup_01.java
        │   └── warmup_01.ts
        ├── solution.py
        ├── Solution.java
        └── solution.ts
```

## 🧠 Workflow

Each problem follows this process:

1. **Analyze** — Break the problem into smaller concepts
2. **Warmup** — Solve mini exercises for each concept (in all 3 languages)
3. **Solve** — Write the final solution (in all 3 languages)
4. **Review** — Add notes to the problem's README.md

## 🗂️ Problem Index

| # | Problem | Difficulty | Python | Java | TypeScript |
|---|---------|------------|--------|------|------------|
| 001 | [Simple Array Sum](problems/001-simple-array-sum/PROBLEM.md) | Easy | ✅ | ❌ | ❌ |
| 002 | [Solve Me First](problems/002-solve-me-first/PROBLEM.md) | Easy | ✅ | ❌ | ❌ |
| 003 | [Compare the Triplets](problems/003-compare-the-triplets/PROBLEM.md) | Easy | ❌ | ❌ | ❌ |

## 🛠️ Languages & Setup

### Python
- Version: 3.x
- Run: `python solution.py`

### Java
- Version: 17+
- Run: `javac Solution.java && java solution`

### TypeScript
- Version: 5.x
- Run: `ts-node solution.ts`

## 📌 Notes
- `archive/java-old/` contains solutions written in 2023 with IntelliJ/Maven setup, kept for reference only.
- Each problem folder has its own README with the original problem link and personal notes.
