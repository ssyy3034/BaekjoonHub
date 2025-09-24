from collections import deque
import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# N: 행, M: 열
N, M = map(int, input().split())

# 맵 정보 입력 (붙어서 들어오므로 rstrip()으로 개행문자 제거)
grid = [list(map(int, input().rstrip())) for _ in range(N)]

# 3차원 visited 배열: visited[x][y][벽 파괴 여부]
# 0: 벽 파괴 안 함, 1: 벽 파괴 함
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    # 큐 초기화: (x, y, 벽 파괴 여부)
    q = deque([(0, 0, 0)])
    # 시작점 방문 처리 (거리 1)
    visited[0][0][0] = 1

    while q:
        x, y, wall_broken = q.popleft()

        # 도착점에 도달하면 현재 거리 반환
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall_broken]

        # 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위를 벗어나지 않는지 확인
            if 0 <= nx < N and 0 <= ny < M:
                # Case 1: 다음 이동할 곳이 벽이 아니고, 아직 방문하지 않았다면
                if grid[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    q.append((nx, ny, wall_broken))

                # Case 2: 다음 이동할 곳이 벽이고, 벽을 아직 부수지 않았다면
                elif grid[nx][ny] == 1 and wall_broken == 0:
                    # 벽을 부수고 방문 처리 (wall_broken 상태를 1로 변경)
                    visited[nx][ny][1] = visited[x][y][wall_broken] + 1
                    q.append((nx, ny, 1))

    # 도착점에 도달할 수 없는 경우
    return -1


print(bfs())