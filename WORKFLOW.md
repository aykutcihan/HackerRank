# Workflow Guide

This file defines how new problems are added and practiced in this repository.
It is used as a reference for both the developer and AI assistants.

---

## 🌐 Communication Rules

- All communication, code, comments, and file content are written in **English**

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
   ├── PROBLEM.md       ← exact problem text + personal notes (single source of truth)
   ├── hints.md         ← layered hints, do not open unless stuck
   ├── notes.md         ← personal learning log, filled after solving
   ├── warmups/
   │   ├── warmup_01_read_input.py     ← templated header inside
   │   ├── warmup_01_read_input.java
   │   └── warmup_01_read_input.ts
   ├── solution.py      ← empty, to be filled after warmups
   ├── Solution.java    ← empty, to be filled after warmups
   └── solution.ts      ← empty, to be filled after warmups
   ```

3. Fill the `PROBLEM.md` with the problem details using the template below.

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
- Developer writes `Solution.java`

### Step 4 — Repeat in TypeScript
- Same warmups repeated in TypeScript (`warmup_01.ts` etc.)
- Developer writes `solution.ts`

### Step 5 — Finalize
- Developer fills in `PROBLEM.md` (approach, complexity, notes section)
- Developer fills in `notes.md` (personal learning log)
- AI updates the Problem Index table in the root `README.md`

---

## 📋 Problem PROBLEM.md Template

When creating a new problem folder, `PROBLEM.md` contains two parts:

**Part 1 — Exact problem text** (copied verbatim from HackerRank, never modified)

**Part 2 — Personal notes** (filled in by developer as they work)

```markdown
# [Problem Name]

**HackerRank Link:** [URL]
**Difficulty:** Easy / Medium / Hard
**Category:** (e.g. Arrays, Strings, Loops)

---

## Problem Statement
[Exact text]

## Input Format / Constraints / Output Format / Sample I/O / Explanation
[Exact text]

---

## 📝 My Summary
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

## 📊 Progress
| Language | Status |
|----------|--------|
| Python | ❌ |
| Java | ❌ |
| TypeScript | ❌ |
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

package warmups;

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

### 📥 When Developer Shares a New Problem

When the developer pastes a HackerRank problem, the AI will immediately:

#### Step 0 — Save the Problem

1. Determine the next problem number from the existing folders under `problems/`
2. Create the folder:
   ```
   problems/NNN-problem-name/
   ```
3. Create `problems/NNN-problem-name/PROBLEM.md` with the EXACT original problem text pasted by the developer — do not summarize, do not paraphrase, copy it word for word including:
   - Problem title
   - Problem description
   - Input format
   - Constraints
   - Output format
   - Sample input / output
   - Explanation (if provided)

   Format:
   ```markdown
   # [Problem Title]

   **HackerRank Link:** [ask developer to paste the URL if not provided]
   **Difficulty:** [Easy / Medium / Hard]
   **Category:** [e.g. Strings, Arrays, Loops]

   ---

   ## Problem Statement
   [Exact problem text here]

   ## Input Format
   [Exact input format here]

   ## Constraints
   [Exact constraints here]

   ## Output Format
   [Exact output format here]

   ## Sample Input
   [Sample input here]

   ## Sample Output
   [Sample output here]

   ## Explanation
   [Explanation if provided]
   ```

4. Also save the HackerRank code template in `PROBLEM.md` under a new section:
   ```
   ## HackerRank Code Template
   [paste the exact code template here]
   ```
   The developer will paste the code editor template shown on the HackerRank problem page.
   This template is problem-specific — it changes every problem.

5. Create solution files automatically from the Java template:
   - `Solution.java` → use the exact HackerRank Java template, add `return 0;` placeholder to the function. **No `package` declaration.**
   - `solution.py` → AI generates this automatically by adapting the Java template to Python (same function name, same I/O logic)
   - `solution.ts` → AI generates this automatically by adapting the Java template to TypeScript (same function name, same I/O logic)
   - Developer only pastes the Java template — AI handles Python and TypeScript
   - `hints.md` (from template)
   - `notes.md` (from template)
   - `warmups/` folder (empty for now)

6. Create the IntelliJ module file `NNN-problem-name.iml` inside the problem folder:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <module type="JAVA_MODULE" version="4">
     <component name="NewModuleRootManager" inherit-compiler-output="true">
       <exclude-output />
       <content url="file://$MODULE_DIR$">
         <sourceFolder url="file://$MODULE_DIR$" isTestSource="false" />
       </content>
       <orderEntry type="inheritedJdk" />
       <orderEntry type="sourceFolder" forTests="false" />
     </component>
   </module>
   ```

7. Register the new module in `.idea/modules.xml` by adding one line inside `<modules>`:
   ```xml
   <module fileurl="file://$PROJECT_DIR$/problems/NNN-problem-name/NNN-problem-name.iml"
           filepath="$PROJECT_DIR$/problems/NNN-problem-name/NNN-problem-name.iml" />
   ```

8. Confirm to the developer which folder was created and show the full folder structure.

9. THEN proceed with the warmup plan analysis.

> **Note:** `PROBLEM.md` is read-only — it is never modified after creation.
> It is the single source of truth for the original problem statement.

---

When the developer shares a HackerRank problem:

1. Read WORKFLOW.md first.
2. Create the problem folder and files (following Step 0 above).
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
13. **Java warmup files must start with `package warmups;`** — this is required for IntelliJ to recognize the file correctly inside the `warmups/` subdirectory. `Solution.java` does NOT get a package declaration.
13. When the problem is fully solved in all 3 languages, update the Problem Index table in the root `README.md` with the new row.

---

## 📊 Problem Index Update Rule

When a problem is fully solved in a language, update the Problem Index table in the root `README.md`:

- ❌ = Not started
- 🔄 = Warmups in progress or solution being written
- ✅ = Solution complete and reviewed

Update the status for each language independently as the developer progresses.
When all three languages show ✅, the problem is considered fully complete.
