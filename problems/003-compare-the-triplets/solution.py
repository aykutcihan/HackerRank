def compareTriplets(a, b):
    num_a = 0
    num_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            num_a += 1
        elif a[i] < b[i]:
            num_b += 1
    return [num_a, num_b]

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(' '.join(map(str, result)))
