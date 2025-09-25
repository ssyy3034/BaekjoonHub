N,K = map(int,input().split())
count = 0
coins = []
for i in range(N):
    coins.append(int(input()))
    coins.sort(reverse=True)

for coin in coins:
    if coin <= K:
        count += K//coin
        K %= coin
        if K <= 0:
            break
print(count)