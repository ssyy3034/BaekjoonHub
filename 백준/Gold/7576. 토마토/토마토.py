from collections import deque

m, n = map(int, input().split())  # m: 열, n: 행
tomato_box = [list(map(int, input().split())) for _ in range(n)]

q = deque()
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 익은 토마토(1) 위치를 모두 큐에 미리 넣는다.
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            q.append((i, j))

# BFS
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
            tomato_box[nx][ny] = tomato_box[x][y] + 1  # 날짜 누적
            q.append((nx, ny))

# 결과 계산
days = 0
for row in tomato_box:
    for t in row:
        if t == 0:  # 아직 안 익은 토마토가 있다면
            print(-1)
            exit(0)
    days = max(days, max(row))

# 처음부터 1로 시작했으므로 -1 해준다.
print(days - 1)
