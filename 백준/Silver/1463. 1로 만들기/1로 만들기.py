K = int(input())

# dp 테이블 초기화 (인덱스를 1부터 사용하기 위해 n+1 크기로)
dp = [-1] * (K + 1)
def recur(n):
    if n == 1:
        return 0

    if dp[n] != -1:
        return dp[n]

    result = 1+recur(n-1)
    if n % 2 == 0:
        result = min(result,recur(n//2)+1)
    if n % 3 == 0:
        result = min(result,recur(n//3)+1)
    dp[n] = result
    return result
print(recur(K))