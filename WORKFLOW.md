# Workflow Guide

This file defines how new problems are added and practiced in this repository.
It is used as a reference for both the developer and AI assistants.

---

## ➕ Adding a New Problem

When a new HackerRank problem is given, the AI assistant will:

1. Create a new folder under `problems/` following this naming convention:
   ```
   problems/NNN-problem-name/
   ```
   Example: `problems/001-java-if-else/`

2. Create the following structure inside that folder:
   ```
   001-java-if-else/
   ├── README.md        ← filled with problem details (see template below)
   ├── hints.md         ← layered hints, do not open unless stuck
   ├── notes.md         ← personal learning log, filled after solving
   ├── warmups/
   │   ├── warmup_01_read_input.py     ← templated header inside
   │   ├── warmup_01_read_input.java
   │   └── warmup_01_read_input.ts
   ├── solution.py      ← empty, to be filled after warmups
   ├── solution.java    ← empty, to be filled after warmups
   └── solution.ts      ← empty, to be filled after warmups
   ```

3. Fill the `README.md` with the problem details using the template below.

4. Analyze the problem and break it into smaller concepts.

5. Prepare the first warmup exercises for each concept — starting with Python.

---

## 🧠 Practice Workflow (Per Problem)

Each problem is solved in this exact order:

### Step 1 — Warmup Phase (Python first)
- AI breaks the problem into sub-concepts
- For each concept, AI creates a warmup exercise
- Developer solves warmups one by one
- AI gives feedback after each solution

### Step 2 — Solve in Python
- Developer writes `solution.py`
- AI reviews and gives feedback

### Step 3 — Repeat in Java
- Same warmups repeated in Java (`warmup_01.java` etc.)
- Developer writes `solution.java`

### Step 4 — Repeat in TypeScript
- Same warmups repeated in TypeScript (`warmup_01.ts` etc.)
- Developer writes `solution.ts`

### Step 5 — Finalize
- Developer fills in `README.md` (approach, complexity, notes)
- Developer fills in `notes.md` (personal learning log)
- AI updates the Problem Index table in the root `README.md`

---

## 📋 Problem README.md Template

When creating a new problem folder, fill README.md with this structure:

```markdown
# [Problem Name]

- **HackerRank Link:** [URL]
- **Difficulty:** Easy / Medium / Hard
- **Category:** (e.g. Arrays, Strings, Loops)

## 📝 Problem Summary
_(Short description in your own words)_

## 🔍 Concepts Needed
- Concept 1
- Concept 2

## 🏋️ Warmup Exercises
| File | Language | What it practices |
|------|----------|-------------------|
| warmup_01 | Python / Java / TS | _(description)_ |

## 💡 My Approach
_(Fill after solving)_

## ⏱️ Complexity
- Time: O(?)
- Space: O(?)
```

---

## 🏋️ Warmup Exercise Design Philosophy

Warmups are NOT just about the problem — they build from the ground up.
The AI will design a warmup ladder that starts from the most basic building block
and climbs step by step toward the final problem.

### Warmup Ladder Structure

Each warmup series follows this progression:

#### Level 1 — Language Basics (if needed)
Pure language fundamentals required for this problem.
Examples:
- How to read input from stdin
- How to print output
- Basic variable types
- For / while loops
- If / else conditions

#### Level 2 — Data Structure Familiarity
The core data structures the problem uses.
Examples:
- How to create and iterate a list/array
- How to use a dictionary/hashmap
- How to work with strings (split, slice, reverse)

#### Level 3 — Core Concept Exercises
Isolated exercises for each concept the problem requires.
Examples:
- "Write a function that finds the max value in a list"
- "Write a function that counts occurrences of each character"

#### Level 4 — Mini Problem
A simplified, smaller version of the actual problem.
Almost identical logic but with reduced complexity.

#### Level 5 — The Real Problem
Developer is now ready to write the final solution.

---

### Warmup File Naming Convention

```
warmups/
├── warmup_01_read_input.py         ← Level 1
├── warmup_02_loop_over_list.py     ← Level 1-2
├── warmup_03_find_max.py           ← Level 3
├── warmup_04_count_chars.py        ← Level 3
├── warmup_05_mini_problem.py       ← Level 4
```

File names describe WHAT is being practiced — not just a number.

---

## 📄 Warmup File Template

Every warmup file is created with a header so the developer knows exactly what to do when they open it, without having to ask.

**Python (`warmup_NN_topic.py`)**
```python
# Warmup NN — [Topic]
# Goal: [One sentence describing what this warmup practices]
#
# Instructions:
# [Clear exercise description here]
#
# Example:
#   Input:  ...
#   Output: ...

# Your solution here:
```

**Java (`warmup_NN_topic.java`)**
```java
// Warmup NN — [Topic]
// Goal: [One sentence describing what this warmup practices]
//
// Instructions:
// [Clear exercise description here]
//
// Example:
//   Input:  ...
//   Output: ...

public class warmup_NN_topic {
    public static void main(String[] args) {
        // Your solution here:
    }
}
```

**TypeScript (`warmup_NN_topic.ts`)**
```typescript
// Warmup NN — [Topic]
// Goal: [One sentence describing what this warmup practices]
//
// Instructions:
// [Clear exercise description here]
//
// Example:
//   Input:  ...
//   Output: ...

// Your solution here:
```

---

## 💡 hints.md Template

Every problem folder includes a `hints.md` with layered hints — do NOT open unless stuck.
Hints are intentionally vague at first and get more specific deeper down.

```markdown
# Hints — [Problem Name]

> Only open the next hint if you are truly stuck. Think first.

<details>
<summary>Hint 1 — Big Picture</summary>

What kind of data structure would make this problem easier?

</details>

<details>
<summary>Hint 2 — Structure</summary>

Think about the loop structure. What are you iterating over, and what are you tracking?

</details>

<details>
<summary>Hint 3 — Edge Cases</summary>

What happens when the input is empty? What if all values are the same?

</details>

<details>
<summary>Hint 4 — Almost There</summary>

[More specific hint — filled by AI when creating the problem]

</details>
```

---

## 📓 notes.md Template

Every problem folder includes a `notes.md` for personal reflections — filled by the developer after solving.

```markdown
# Notes — [Problem Name]

## Where I Got Stuck
_(What was the hardest part? Where did you spend the most time?)_

## Python vs Java vs TypeScript
_(What syntax or logic differences did you notice across languages?)_

## What I'd Do Differently
_(If you solved this again from scratch, what would you change?)_

## Key Takeaway
_(One sentence: what did this problem teach you?)_
```

---

## 🤖 Instructions for AI Assistants

When the developer shares a HackerRank problem:

1. Read WORKFLOW.md first.
2. Create the problem folder and files.
3. Analyze the problem deeply:
   - What language basics are needed?
   - What data structures are used?
   - What is the core algorithm/logic?
   - What is the hardest part of the problem?
4. Design a warmup ladder (Level 1 → Level 5) BEFORE starting.
5. Show the developer the full warmup plan first — get approval.
6. Then start with warmup_01 — give the exercise, wait for the solution.
7. After each solution:
   - Give feedback (correct / needs fix / can be improved)
   - Explain WHY the approach works or doesn't
   - Only move to next warmup after current one is solid
8. Do NOT skip levels even if the problem seems simple.
9. Do NOT give the solution directly at any point.
10. After all warmups are done in Python → repeat ladder in Java.
11. After Java → repeat ladder in TypeScript.
12. Note: Java and TypeScript warmups can move faster since the logic is already understood — focus on language syntax differences.
13. When the problem is fully solved in all 3 languages, update the Problem Index table in the root `README.md` with the new row.
