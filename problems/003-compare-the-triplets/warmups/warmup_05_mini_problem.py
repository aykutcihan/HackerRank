# Warmup 05 — Mini Problem
# Goal: Full flow — read two lists from stdin, compare them, return and print scores.
#
# Instructions:
# 1. Define a function called scoreCount(a, b) that compares the two lists
#    and returns [alice_score, bob_score].
# 2. Read two lines of space-separated integers from stdin.
# 3. Call scoreCount and print the result as two space-separated numbers.
#
# Example:
#   Input:  5 6 7
#           3 6 10
#   Output: 1 1

def scoreCount(a, b):
    alice_score = 0
    bob_score = 0
    for num_a, num_b in zip(a, b):
        if num_a > num_b:
            alice_score += 1
        elif num_a < num_b:
            bob_score += 1
    return [alice_score, bob_score]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = scoreCount(a, b)
print(result[0], result[1])