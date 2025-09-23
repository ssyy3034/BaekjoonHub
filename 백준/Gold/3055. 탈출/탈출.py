from collections import deque

r,c = map(int,input().split())

grid = []
for _ in range(r):
    grid.append(list(input()))

visited = [[0 for _ in range(c)]for _ in range(r)]
start_x = 0
start_y = 0
q = deque()
for x in range(r):
    for y in range(c):
        if grid[x][y] == "*":
            q.append((x,y))
        if grid[x][y] == 'S':
            start_x = x
            start_y = y
q.append((start_x,start_y))
time = 0
visited[start_x][start_y] = 1
dx = [1,-1,0,0]
dy = [0,0,-1,1]

while q:
    hog_next_q = deque()
    water_next_q = deque()

    q_size = len(q)
    for _ in range(q_size):
        nx, ny = q.popleft()

        if grid[nx][ny] != '*':
            for i in range(4):
                xx = nx + dx[i]
                yy = ny + dy[i]
                
                if not (0 <= xx < r and 0 <= yy < c):
                    continue
                
                if grid[xx][yy] == 'D':
                    print(time + 1)
                    exit(0)
                
                if grid[xx][yy] == '.' and not visited[xx][yy]:
                    visited[xx][yy] = 1
                    hog_next_q.append((xx, yy))
        
        else:
            for i in range(4):
                xx = nx + dx[i]
                yy = ny + dy[i]
                
                if 0 <= xx < r and 0 <= yy < c and grid[xx][yy] == '.':
                    water_next_q.append((xx, yy))

    for wx, wy in water_next_q:
        if grid[wx][wy] == '.':
            grid[wx][wy] = '*'
            q.append((wx, wy))
            
    for hx, hy in hog_next_q:
        q.append((hx, hy))

    time += 1

print('KAKTUS')