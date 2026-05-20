# Warmup 02 — Compare Two Numbers
# Goal: Read two integers and determine which is greater (or if they are equal).
#
# Instructions:
# Read two integers (one per line). Print:
#   "first"  — if the first is greater
#   "second" — if the second is greater
#   "equal"  — if they are the same
#
# Example:
#   Input:  7
#           3
#   Output: first


first = int(input())
second = int(input())

if first > second:
    print("first")
elif first < second:
    print("second")
else:
    print("equal")