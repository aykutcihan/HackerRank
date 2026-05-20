# Warmup 03 — Zip Two Lists
# Goal: Iterate over two lists in parallel using zip() and print each pair.
#
# Instructions:
# You are given two hardcoded lists:
#   a = [5, 6, 7]
#   b = [3, 6, 10]
# Use zip(a, b) to iterate over both at the same time.
# Print each pair on one line as: "a=5, b=3"
#
# Example:
#   Output: a=5, b=3
#           a=6, b=6
#           a=7, b=10


a = [5, 6, 7]
b = [3, 6, 10]

for num_a, num_b in zip(a, b):
    print(f"a={num_a}, b={num_b}")