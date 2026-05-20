# Warmup 04 — Mini Problem
# Goal: Combine input reading and a function to produce the final output.
#
# Instructions:
# 1. Define a function called sumTwo(a, b) that returns a + b.
# 2. Read two integers from stdin (one per line).
# 3. Call sumTwo with those two integers.
# 4. Print the result.
#
# Example:
#   Input:  2
#           3
#   Output: 5

def sumTwo(a, b):
    return a + b

first = int(input())
second = int(input())
print(sumTwo(first, second))