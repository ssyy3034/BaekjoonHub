import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
small = set(int(input()) for _ in range(M))

if N == 1:
    print(0)
    sys.exit(0)

max_v = int((2 * N) ** 0.5) + 2  # 속도 상한 (√(2N) 근사)
vis = [[False] * (max_v + 1) for _ in range(N + 1)]

q = deque()
q.append((1, 0))  # (현재 돌, 현재 속도)
vis[1][0] = True
steps = 0

while q:
    for _ in range(len(q)):
        x, v = q.popleft()
        for nv in (v - 1, v, v + 1):
            if nv <= 0 or nv > max_v:
                continue
            nx = x + nv
            if nx > N or nx in small:
                continue
            if nx == N:
                print(steps + 1)
                sys.exit(0)
            if not vis[nx][nv]:
                vis[nx][nv] = True
                q.append((nx, nv))
    steps += 1

print(-1)
