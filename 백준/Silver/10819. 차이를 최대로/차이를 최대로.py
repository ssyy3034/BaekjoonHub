from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

max_sum = 0

for p in permutations(numbers):
    current_sum = 0
    for i in range(n - 1):
        current_sum += abs(p[i] - p[i + 1])
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)