from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2 = map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False]*(n+1)
dfs_result = []

def dfs(v):

    visited_dfs[v] = True
    dfs_result.append(v)
    for next in graph[v]:
        if not visited_dfs[next]:
            dfs(next)

visited_bfs = [False]*(n+1)
bfs_result = []
def bfs(start_v):
    q = deque([start_v])
    visited_bfs[start_v] = True
    while q:
        v = q.popleft()
        bfs_result.append(v)
        for next in graph[v]:
            if not visited_bfs[next]:
                q.append(next)
                visited_bfs[next] = True
dfs(v)
bfs(v)
print(*dfs_result)
print(*bfs_result)

