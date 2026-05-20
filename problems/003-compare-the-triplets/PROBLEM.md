# Compare the Triplets

**HackerRank Link:** https://www.hackerrank.com/challenges/compare-the-triplets/problem
**Difficulty:** Easy
**Category:** Algorithms, Warmup

---

## Problem Statement

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to calculate their comparison points by comparing each category:

- If a[i] > b[i], then Alice is awarded 1 point.
- If a[i] < b[i], then Bob is awarded 1 point.
- If a[i] = b[i], then neither person receives a point.

## Function Description

Complete the function `compareTriplets` with the following parameters:

- *int a[3]*: Alice's challenge rating
- *int b[3]*: Bob's challenge rating

**Returns**

- *int[2]*: the first element is Alice's score and the second is Bob's score

## Input Format

The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

## Constraints

- 1 ≤ a[i] ≤ 100
- 1 ≤ b[i] ≤ 100

## Sample Input 0

```
5 6 7
3 6 10
```

## Sample Output 0

```
1 1
```

## Explanation 0

- a = (5, 6, 7), b = (3, 6, 10)
- a[0] > b[0], so Alice receives 1 point.
- a[1] = b[1], so nobody receives a point.
- a[2] < b[2], so Bob receives 1 point.

Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we return the array [1, 1].

## Sample Input 1

```
17 28 30
99 16 8
```

## Sample Output 1

```
2 1
```

## Explanation 1

Comparing the 0th elements, 17 < 99 so Bob receives a point.
The 1st and 2nd elements, 28 > 16 and 30 > 8 so Alice receives two points.
The return array is [2, 1].

## HackerRank Code Template (Python)

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```

---

## 📝 My Summary
_(Short description in your own words)_

## 🔍 Concepts Needed
- Reading space-separated integers into a list
- Iterating over two lists in parallel
- Comparing elements and tracking scores
- Returning a list and printing it as space-separated values

## 🏋️ Warmup Exercises
| File | Language | What it practices |
|------|----------|-------------------|
| warmup_01_read_space_separated | Python | Read a line of space-separated ints into a list |
| warmup_02_compare_two_numbers | Python | Compare two integers, determine the winner |
| warmup_03_zip_two_lists | Python | Iterate over two lists in parallel with zip |
| warmup_04_count_wins | Python | Count wins for each side from hardcoded lists |
| warmup_05_mini_problem | Python | Full flow: read two lists, compare, print scores |

## 💡 My Approach
_(Fill after solving)_

## ⏱️ Complexity
- Time: O(1) — always exactly 3 comparisons
- Space: O(1)

## 📊 Progress
| Language | Status |
|----------|--------|
| Python | ❌ |
