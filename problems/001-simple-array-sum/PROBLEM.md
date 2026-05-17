# Simple Array Sum

**HackerRank Link:** https://www.hackerrank.com/challenges/simple-array-sum/problem
**Difficulty:** Easy
**Category:** Arrays, Loops

---

## Problem Statement

Given an array of integers, find the sum of its elements.

For example, if the array ar = [1, 2, 3], 1 + 2 + 3 = 6, so return 6.

**Function Description**

Complete the simpleArraySum function with the following parameter(s):
- ar[n]: an array of integers

**Returns**
- int: the sum of the array elements

## Input Format

The first line contains an integer, n, denoting the size of the array.
The second line contains n space-separated integers representing the array's elements.

## Constraints

0 < n, ar[i] ≤ 1000

## Output Format

Print the sum of the array's elements.

## Sample Input
```
6
1 2 3 4 10 11
```

## Sample Output
```
31
```

## Explanation

Print the sum of the array's elements: 1 + 2 + 3 + 4 + 10 + 11 = 31.

## HackerRank Code Template (C++)
```cpp
#include <bits/stdc++.h>
using namespace std;

int simpleArraySum(vector<int> ar) {

}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    string ar_count_temp;
    getline(cin, ar_count_temp);
    int ar_count = stoi(ltrim(rtrim(ar_count_temp)));
    string ar_temp_temp;
    getline(cin, ar_temp_temp);
    vector<string> ar_temp = split(rtrim(ar_temp_temp));
    vector<int> ar(ar_count);
    for (int i = 0; i < ar_count; i++) {
        ar[i] = stoi(ar_temp[i]);
    }
    int result = simpleArraySum(ar);
    fout << result << "\n";
    fout.close();
    return 0;
}
```

---

## 📝 My Summary
_(Short description in your own words)_

## 🔍 Concepts Needed
- Reading integer input from stdin
- Reading space-separated integers into a list
- Iterating over a list with a loop
- Accumulating a running total

## 🏋️ Warmup Exercises
| File | Language | What it practices |
|------|----------|-------------------|
| warmup_01_read_integer | Python / Java / TS | Reading a single integer from stdin |
| warmup_02_read_list | Python / Java / TS | Reading space-separated integers into a list |
| warmup_03_loop_sum | Python / Java / TS | Summing a hardcoded list with a for loop |
| warmup_04_mini_problem | Python / Java / TS | Full input/output flow without built-in sum |

## 💡 My Approach
_(Fill after solving)_

## ⏱️ Complexity
- Time: O(?)
- Space: O(?)

## 📊 Progress
| Language | Status |
|----------|--------|
| Python | ✅ |
| Java | ❌ |
| TypeScript | ❌ |
