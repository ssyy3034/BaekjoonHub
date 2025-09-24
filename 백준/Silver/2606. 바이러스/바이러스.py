from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 0:
            dfs(nxt)
dfs(1)
count = 0
for t in visited:
    if t:
        count+=1
print(count-1)