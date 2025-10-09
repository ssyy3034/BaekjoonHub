from collections import deque
n,m,k = map(int,input().split())
field = [[0] * (m+1) for _ in range(n+1)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(k):
    x, y = map(int, input().split())
    field[x][y] = 1

def bfs(sx,sy):
    q = deque([(sx,sy)])
    field[sx][sy] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 1<=nx<=n and 1<=ny<=m and field[nx][ny] == 1:
                field[nx][ny] = 0
                cnt+=1
                q.append((nx,ny))
    return cnt
ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if field[i][j] == 1:
            ans = max(ans,bfs(i,j))

print(ans)



