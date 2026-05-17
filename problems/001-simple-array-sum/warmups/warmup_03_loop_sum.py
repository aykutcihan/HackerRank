# Warmup 03 — Sum a List With a Loop
# Goal: Practice accumulating a total using a for loop (no built-in sum()).
#
# Instructions:
#   The list below is already given — do NOT change it.
#   Write a for loop that adds up all the numbers.
#   Print the total.
#
# Expected output: 28

numbers = [4, 8, 1, 6, 5, 4]

# Your solution here:

sum = 0
for num in numbers:
    sum +=num
print(sum)