import sys
from collections import deque

# 보드의 크기 N
n = int(sys.stdin.readline())
# 사과의 개수 K
k = int(sys.stdin.readline())

# 보드 정보 (0: 빈칸, 1: 사과, 2: 뱀)
board = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1

# 방향 변환 정보
l = int(sys.stdin.readline())
turns = {}
for _ in range(l):
    x, c = sys.stdin.readline().split()
    turns[int(x)] = c

# 동, 남, 서, 북 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def simulate():
    # 뱀의 초기 위치와 방향
    x, y = 0, 0
    board[x][y] = 2  # 뱀이 있는 위치는 2로 표시
    direction = 0  # 초기 방향: 동쪽
    time = 0

    # 뱀의 몸통 정보 (꼬리 -> 머리 순서)
    snake = deque([(x, y)])

    while True:
        # 다음 머리 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 시간 증가
        time += 1

        # 벽에 부딪히거나 자기 몸에 부딪히면 게임 종료
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            break

        # 이동한 칸에 사과가 없는 경우
        if board[nx][ny] == 0:
            # 꼬리 제거
            px, py = snake.popleft()
            board[px][py] = 0

        # 새로운 머리 위치로 이동
        board[nx][ny] = 2
        snake.append((nx, ny))
        x, y = nx, ny

        # 해당 시간에 방향 전환 정보가 있다면 방향 전환
        if time in turns:
            if turns[time] == 'L':  # 왼쪽으로 90도 회전
                direction = (direction - 1) % 4
            else:  # 오른쪽으로 90도 회전
                direction = (direction + 1) % 4

    return time


print(simulate())