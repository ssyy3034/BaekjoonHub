import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    reversed_graph[end].append((start, time))

def dijkstra(start_node, target_graph):
    distances = [INF] * (n + 1)
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)
        
        if distances[current_node] < dist:
            continue
        
        for next_node, next_dist in target_graph[current_node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(priority_queue, (cost, next_node))
                
    return distances

dist_from_X = dijkstra(x, graph)
dist_to_X = dijkstra(x, reversed_graph)

max_round_trip_time = 0

for i in range(1, n + 1):
    round_trip_time = dist_to_X[i] + dist_from_X[i]
    if round_trip_time > max_round_trip_time:
        max_round_trip_time = round_trip_time

print(max_round_trip_time)