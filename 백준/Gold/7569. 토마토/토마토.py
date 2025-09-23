import sys
from collections import deque

# 입력 받기
m, n, h = map(int, sys.stdin.readline().split())
box = []
queue = deque()

# 3차원 상자 정보 입력 및 초기 익은 토마토 큐에 추가
for i in range(h):
    floor = []
    for j in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if row[k] == 1:
                # 큐에는 (높이, 세로, 가로) 순으로 좌표를 저장
                queue.append((i, j, k))
        floor.append(row)
    box.append(floor)

# 이동할 여섯 방향 (상, 하, 좌, 우, 앞, 뒤)
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        # 현재 토마토의 위치를 큐에서 꺼냄
        ch, cn, cm = queue.popleft()

        # 여섯 방향으로 탐색
        for i in range(6):
            nh, nn, nm = ch + dh[i], cn + dn[i], cm + dm[i]

            # 상자 범위를 벗어나지 않고, 익지 않은 토마토가 있다면
            if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m and box[nh][nn][nm] == 0:
                # 새로운 토마토를 익게 하고, 날짜를 하루 증가시켜 기록
                box[nh][nn][nm] = box[ch][cn][cm] + 1
                # 새로 익은 토마토를 큐에 추가
                queue.append((nh, nn, nm))

# BFS 실행
bfs()

max_day = 0
# 모든 탐색이 끝난 후 결과 확인
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 만약 익지 않은 토마토(0)가 남아있다면
            if box[i][j][k] == 0:
                print(-1)
                exit(0) # 프로그램 즉시 종료
            # 가장 늦게 익은 토마토의 날짜를 찾음
            max_day = max(max_day, box[i][j][k])

# 처음 모든 토마토가 익어있던 상태(1)를 빼서 실제 걸린 날짜 계산
print(max_day - 1)