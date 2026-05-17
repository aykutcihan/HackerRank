# Warmup 05 — Read N, Then Build a List
# Goal: Read a count first, then read that many numbers into a list.
#
# Instructions:
#   First line: one integer n (how many numbers will follow)
#   Second line: n space-separated integers
#   Print the list.
#
# Example:
#   Input:
#     3
#     10 20 30
#   Output:
#     [10, 20, 30]
#
#   Input:
#     5
#     4 8 1 6 5
#   Output:
#     [4, 8, 1, 6, 5]

# Your solution here:

# n = int(input())
# numbers = []
# for i in range(n):
#     num = int(input())
#     numbers.append(num)
# print(numbers)


n = int(input())
numbers = list(map(int, input().split()))
print(numbers)