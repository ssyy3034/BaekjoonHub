import sys

list_a = sys.stdin.readline().strip()
list_b = sys.stdin.readline().strip()

A = len(list_a)
B = len(list_b)


dp = [[0 for _ in range(B + 1)] for _ in range(A + 1)]

for i in range(1, A + 1):
    for j in range(1, B + 1):
        if list_a[i-1] == list_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[A][B])