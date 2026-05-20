# Warmup 04 — Count Wins
# Goal: Compare two hardcoded lists element by element and count wins for each side.
#
# Instructions:
# You are given two hardcoded lists:
#   a = [5, 6, 7]
#   b = [3, 6, 10]
# For each index i:
#   - if a[i] > b[i]: alice_score += 1
#   - if a[i] < b[i]: bob_score += 1
#   - if equal: no points
# Print alice_score and bob_score at the end.
#
# Example:
#   Output: Alice: 1
#           Bob: 1
 
a = [5, 6, 7]
b = [3, 6, 10]

alice_score = 0
bob_score = 0

for num_a, num_b in zip(a, b):
    if num_a > num_b:
        alice_score += 1
    elif num_a < num_b:
        bob_score += 1

print(f"Alice: {alice_score}")
print(f"Bob: {bob_score}")

