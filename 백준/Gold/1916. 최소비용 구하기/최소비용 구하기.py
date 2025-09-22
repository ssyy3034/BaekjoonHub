import heapq
from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
dist = [1e9 for i in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    start,end,weight = map(int, input().split())
    graph[start].append((end,weight))
start_city,end_city = map(int, input().split())

def bfs(start):
    q= []
    dist[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        cur_cost,cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_cost:

            continue
        for neighbor,weight in graph[cur_node]:
            new_cost = cur_cost +weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(q,(new_cost,neighbor))
bfs(start_city)
print(dist[end_city])
