def recur(start,i):

    if i == m:
        print(*arr)
        return

    for j in range(start, n+1):
        arr.append(j)
        recur(j,i+1)
        arr.pop()

arr = []

n, m = map(int, input().split())
visited = [0 for _ in range(n+1)]
start = 0

recur(1,0)