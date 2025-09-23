import sys
from collections import deque

readline = sys.stdin.readline


def bfs(start_node, graph, color):

    q = deque([start_node])  # 시작 노드를 큐에 넣음
    color[start_node] = 1  # 시작 노드를 1번 색으로 칠함

    while q:
        curr_node = q.popleft()

        for nxt_node in graph[curr_node]:
            # 아직 방문하지 않은 노드라면
            if color[nxt_node] == 0:
                # 현재 노드와 반대 색으로 칠함 (1 -> 2, 2 -> 1)
                color[nxt_node] = 3 - color[curr_node]
                q.append(nxt_node)
            # 이미 방문했는데, 인접 노드와 색이 같다면
            elif color[nxt_node] == color[curr_node]:
                return False  # 이분 그래프가 아님! 즉시 False 반환

    return True  # 충돌 없이 탐색이 끝났다면 이분 그래프 조건 만족


# ----------------- 메인 로직 -----------------

K = int(readline())
for _ in range(K):
    V, E = map(int, readline().split())
    graph = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)  # 0: 미방문, 1: 색1, 2: 색2

    for _ in range(E):
        u, v = map(int, readline().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    # 모든 정점을 확인하며, 방문하지 않은 정점에서 새로운 BFS 시작 (연결되지 않은 그래프 처리)
    for i in range(1, V + 1):
        if color[i] == 0:
            # bfs 함수의 결과가 False라면, 전체가 이분 그래프가 아님
            if not bfs(i,graph, color):
                is_bipartite = False
                break  # 더 이상 확인할 필요 없음

    if is_bipartite:
        print("YES")
    else:
        print("NO")