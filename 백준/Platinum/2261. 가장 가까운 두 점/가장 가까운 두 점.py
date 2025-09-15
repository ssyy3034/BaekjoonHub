import sys

# 재귀 깊이 제한 늘리기
sys.setrecursionlimit(10 ** 6)


def dist_sq(p1, p2):
    """ 두 점 사이의 거리의 '제곱'을 반환하는 함수 """
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def find_closest_pair(points, n):
    """ 분할 정복으로 가장 가까운 두 점 사이의 거리를 찾는 함수 """
    # 점이 3개 이하일 경우, 브루트포스로 직접 계산 (재귀의 베이스 케이스)
    if n <= 3:
        min_d = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                d = dist_sq(points[i], points[j])
                min_d = min(min_d, d)
        return min_d

    # 1. 분할 (Divide)
    mid_idx = n // 2
    mid_x = points[mid_idx][0]

    # 2. 정복 (Conquer)
    d_left = find_closest_pair(points[:mid_idx], mid_idx)
    d_right = find_closest_pair(points[mid_idx:], n - mid_idx)

    d = min(d_left, d_right)

    # 3. 결합 (Combine)
    # 중앙 분할선을 기준으로 d 거리 이내에 있는 점들(후보)을 찾는다.
    candidate_points = []
    for i in range(n):
        if (points[i][0] - mid_x) ** 2 < d:
            candidate_points.append(points[i])

    # 후보 점들을 y좌표 기준으로 정렬
    candidate_points.sort(key=lambda p: p[1])

    # y좌표 기준으로 정렬된 후보 점들을 순회하며 최소 거리를 찾는다.
    len_cand = len(candidate_points)
    for i in range(len_cand - 1):
        for j in range(i + 1, len_cand):
            # 두 점의 y좌표 차이가 d보다 크면 더 이상 볼 필요 없음
            if (candidate_points[j][1] - candidate_points[i][1]) ** 2 >= d:
                break

            d_cand = dist_sq(candidate_points[i], candidate_points[j])
            d = min(d, d_cand)

    return d


# --- 입력 처리 ---
N = int(sys.stdin.readline())
# 중복된 점을 제거하고 x좌표 기준으로 정렬
# set으로 중복 제거 후 다시 list로 변환, 그리고 정렬
points_set = set()
for _ in range(N):
    points_set.add(tuple(map(int, sys.stdin.readline().split())))
points = sorted(list(points_set))

# 만약 중복된 점이 있었다면 거리는 0
if len(points) != N:
    print(0)
else:
    # 함수 실행 및 결과 출력
    min_dist_sq = find_closest_pair(points, len(points))
    print(min_dist_sq)