  # Warmup 01 — Read Space-Separated Integers
# Goal: Read a single line of space-separated integers and store them in a list.
#
# Instructions:
# Read one line of input containing 3 space-separated integers.
# Store them in a list and print each element on its own line.
#
# Example:
#   Input:  5 6 7
#   Output: 5
#           6
#           7

numbers = list(map(int, input().split()))
for num in numbers:
    print(num)
