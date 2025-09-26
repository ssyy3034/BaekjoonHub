tc = int(input())

for _ in range(tc):
    N = int(input())
    coin_list =list(map(int,input().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for coin in coin_list:
        for i in range(coin,target+1):
            dp[i] += dp[i-coin]
    print(dp[target])
