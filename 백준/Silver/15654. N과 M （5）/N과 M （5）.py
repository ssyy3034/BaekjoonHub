def recur(i):
    if i == m:
        print(*arr)
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            arr.append(n_list[j])

            recur(i+1)
            arr.pop()
            visited[j] = 0
arr = []

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
visited = [0 for _ in range(n+1)]


recur(0)