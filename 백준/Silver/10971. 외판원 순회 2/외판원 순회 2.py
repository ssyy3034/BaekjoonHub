N = int(input())
t_list = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
min_sum = 10000000

def dfs(here, cnt, cost):
    global min_sum
    if cost >= min_sum:
        return

    if cnt == N:
        if t_list[here][0] != 0:
            min_sum = min(min_sum, cost + t_list[here][0])
        return

    for nxt in range(N):
        if (not visited[nxt]) and t_list[here][nxt] != 0:
            visited[nxt] = True
            dfs(nxt, cnt + 1, cost + t_list[here][nxt])
            visited[nxt] = False

visited[0] = True
dfs(0, 1, 0)
print(min_sum)
