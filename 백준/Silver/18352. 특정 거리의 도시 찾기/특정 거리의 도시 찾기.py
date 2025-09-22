from collections import deque
import sys


input = sys.stdin.readline

n, m, k, x = map(int, input().split())
city_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    city_list[a].append(b)

distance = [-1] * (n + 1)

def bfs(start):
    q = deque([start])
    distance[start] = 0

    while q:
        now = q.popleft()

        for next_node in city_list[now]:
            if distance[next_node] == -1:

                distance[next_node] = distance[now] + 1
                q.append(next_node)

bfs(x)


answer = []
for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    for city in answer:
        print(city)