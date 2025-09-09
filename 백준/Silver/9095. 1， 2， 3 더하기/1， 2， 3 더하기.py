dp = [0]*12

dp[1] = 1
dp[2] = 2
dp[3] = 4

    # 반복문으로 dp 배열 채우기
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

tc = int(input())
for i in range(tc):
    n = int(input())
    print(dp[n])





