from collections import deque

n, m = map(int, input().split())
field = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while q:
        current_x, current_y = q.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m:
                if field[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = visited[current_x][current_y] + 1
                    q.append((next_x, next_y))

    return visited[n - 1][m - 1]


print(bfs(0, 0))