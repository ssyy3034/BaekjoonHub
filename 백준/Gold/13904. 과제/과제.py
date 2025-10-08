n = int(input())
sub = []

for i in range(n):
    d,w = map(int,input().split())
    sub.append((w,d))
sub.sort(reverse=True)
max_day = 0
for g in sub:
    max_day = max(max_day,g[1])
answer = [0 for i in range(max_day+1)]
for g in sub:
    if answer[g[1]] == 0:
        answer[g[1]] = g[0]
    else:
        a = g[1]
        while a>0:
            if answer[a] == 0:
                answer[a] = g[0]
                break
            a -=1
print(sum(answer))
