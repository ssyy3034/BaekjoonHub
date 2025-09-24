import sys

# 입력 처리
n = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 상, 하, 좌, 우 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    """
    현재 위치(x, y)와 연결된 모든 집의 개수를 세어 반환하는 함수.
    """
    # 현재 위치를 방문 처리
    visited[x][y] = True

    # 자기 자신을 포함하여 단지 내 집의 수를 1로 초기화
    count = 1

    # 현재 위치에서 네 방향(상, 하, 좌, 우)을 확인
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 지도를 벗어나지 않는지 확인
        if 0 <= next_x < n and 0 <= next_y < n:
            # 아직 방문하지 않은 집이 있다면
            if field[next_x][next_y] == 1 and not visited[next_x][next_y]:
                # 재귀적으로 호출하고, 반환된 값을 현재 count에 더함
                count += dfs(next_x, next_y)

    # 탐색이 끝난 후, 총 집의 수를 반환
    return count


# 각 단지에 속하는 집의 수를 저장할 리스트
danji_counts = []

# 지도의 모든 위치를 확인
for i in range(n):
    for j in range(n):
        # 만약 해당 위치에 집이 있고(1) 아직 방문하지 않았다면
        if field[i][j] == 1 and not visited[i][j]:
            # 새로운 단지를 발견했으므로 DFS 탐색을 시작하고,
            # 반환된 단지 내 집의 수를 리스트에 추가
            danji_counts.append(dfs(i, j))

# 문제의 요구사항에 맞게 단지 내 집의 수를 오름차순으로 정렬
danji_counts.sort()

# 총 단지 수 출력
print(len(danji_counts))

# 각 단지별 집의 수를 한 줄에 하나씩 출력
for count in danji_counts:
    print(count)