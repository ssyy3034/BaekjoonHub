import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline

# 1. 입력 처리 (변경 없음)
n = int(readline())
locations = [0] + list(map(int, readline().rstrip()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, readline().split())
    graph[u].append(v)
    graph[v].append(u)

total_count = 0


for i in range(1, n + 1):
    if locations[i] == 0:  
        indoor_neighbors = 0

        for neighbor in graph[i]:
            if locations[neighbor] == 1:
                indoor_neighbors += 1

        total_count += indoor_neighbors * (indoor_neighbors - 1)


visited = [False] * (n + 1)
for i in range(1, n + 1):
    if locations[i] == 1 and not visited[i]:
        component_size = 0
        q = deque([i])
        visited[i] = True

        while q:
            curr_node = q.popleft()
            component_size += 1
            for neighbor in graph[curr_node]:
                if locations[neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        total_count += component_size * (component_size - 1)

# 최종 결과 출력
print(total_count)