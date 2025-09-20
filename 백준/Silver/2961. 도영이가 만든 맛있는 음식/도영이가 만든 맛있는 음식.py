def recur(idx, sin, cos,use):
    global answer
    if idx == n:
        if use == 0:
            return
        result = abs(sin - cos)
        answer = min(answer,result)
        return

    recur(idx + 1, sin * ingre[idx][0], cos + ingre[idx][1],use+1)
    recur(idx + 1, sin, cos,use)


n = int(input())
ingre = [list(map(int, input().split()))for _ in range(n)]
answer = 10**6

recur(0,1,0,0)
print(answer)