dp = [0]*12
def case(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    if dp[x] >0:
        return dp[x]
    dp[x] =  case(x-1) + case(x-2) + case(x-3)
    return dp[x]

tc = int(input())
for i in range(tc):
    n = int(input())
    print(case(n))





