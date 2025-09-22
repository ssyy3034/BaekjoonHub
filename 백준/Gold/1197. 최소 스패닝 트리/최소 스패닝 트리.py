import sys

sys.setrecursionlimit(10**6)
# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline


# 특정 원소가 속한 집합의 대표(루트)를 찾는 함수
def find_parent(parent, x):
    # 만약 x가 자기 자신을 부모로 가지지 않는다면, 더 상위 부모를 찾아 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축(Path Compression) 최적화
    return parent[x]


# 두 원소가 속한 집합을 합치는 함수 (두 반을 하나로 합치기)
def union_parent(parent, a, b):
    # a와 b의 대표를 각각 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 번호를 가진 대표를 부모로 삼아 두 집합을 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 정점(v)과 간선(e)의 개수를 입력받음
v, e = map(int, input().split())

# 부모 테이블 초기화 (처음에는 모든 정점이 자기 자신을 대표로 가짐)
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선 정보를 입력받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해 비용을 튜플의 첫 번째 원소로 저장
    edges.append((cost, a, b))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

# 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 두 노드의 대표(루트)가 서로 다르다면 (아직 같은 집합이 아니라면)
    if find_parent(parent, a) != find_parent(parent, b):
        # 두 집합을 합치고 (간선을 트리에 포함)
        union_parent(parent, a, b)
        # 해당 간선의 비용을 결과에 더함
        result += cost

# 최종 비용 출력
print(result)