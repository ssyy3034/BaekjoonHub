N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
min_cost = 100000000000
visited = [False] * N

def search(curr, cnt,cost):
    global min_cost
    if cost >= min_cost:
        return

    if cnt == N:
        if W[curr][0] != 0:
            min_cost = min(min_cost,cost+W[curr][0])
        return

    for nxt in range(N):
        if not visited[nxt] and W[curr][nxt] != 0:
            visited[nxt] = True
            search(nxt, cnt + 1,cost + W[curr][nxt])
            visited[nxt] = False

visited[0] = True
search(0,1,0)
print(min_cost)




