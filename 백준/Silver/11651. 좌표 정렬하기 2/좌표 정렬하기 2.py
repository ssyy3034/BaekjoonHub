n = int(input())
cases = []
for i in range(n):
    x,y = map(int, input().split())
    cases.append((x,y))
cases.sort(key=lambda t: (t[1],t[0]))

for i in range(n):
    print(*cases[i])
