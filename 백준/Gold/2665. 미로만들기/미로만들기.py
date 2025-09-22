import sys
from collections import deque

n = int(sys.stdin.readline())

maze = [list(map(int,sys.stdin.readline().rstrip()))for _ in range(n)]

dist = [[-1] *n for _ in range(n)]
q = deque()

q.append((0,0))
dist[0][0] = 0

dx = [1,-1,0,0]
dy = [0,0,-1,1]
while q:
    x,y =q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx < n and 0<= ny < n:
            if dist[nx][ny] == -1:
                if maze[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
print(dist[n-1][n-1])


