N, K = map(int, input().split())
items = []  # (무게, 가치)
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = items[i - 1]
    for k in range(K + 1):
        dp[i][k] = dp[i - 1][k]
        if k >= W:
            dp[i][k] = max(dp[i][k], dp[i - 1][k - W] + V)

print(dp[N][K])
