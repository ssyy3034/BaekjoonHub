N = int(input())
dp = [-1 for _ in range(1_000_001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(3,N+2):
    dp[i] = (dp[i-1]+dp[i-2])%10007

print(dp[N])