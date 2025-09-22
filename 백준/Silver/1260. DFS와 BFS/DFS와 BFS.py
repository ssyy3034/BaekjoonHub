import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    graph[i].sort()

dfs_visited = [0 for _ in range(n+1)]
dfs_result = []


def dfs(node):
    dfs_visited[node] = 1
    dfs_result.append(node)

    for nxt in graph[node]:
        if not dfs_visited[nxt]:
            dfs(nxt)

bfs_visited = [0 for _ in range(n+1)]
bfs_result = []

def bfs(node):
    q = deque()
    q.append(node)
    bfs_visited[node] = 1
    while q:
        curr = q.popleft()
        bfs_result.append(curr)
        for nxt in graph[curr]:
            if not bfs_visited[nxt]:
                q.append(nxt)
                bfs_visited[nxt] = 1


dfs(v)
bfs(v)

print(*dfs_result)
print(*bfs_result)

