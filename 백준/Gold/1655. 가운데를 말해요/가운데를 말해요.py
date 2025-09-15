import sys
import heapq


input = sys.stdin.readline 

# 숫자의 개수 N 입력
n = int(input())

# 최대 힙(max_heap)과 최소 힙(min_heap)으로 사용할 리스트
max_heap = []  # 중간값보다 작은 그룹 (내림차순) 왜냐, 가장 높은수가 heap의 top이기때문
min_heap = []  # 중간값보다 큰 그룹 (오름차순) 왜냐, 가장 낮은수가 heap의 top이기때문

# N개의 숫자를 하나씩 처리
for _ in range(n):
    num = int(input())

    # 1. 숫자 넣기: 크기 균형 규칙에 따라 힙에 숫자 추가
    # 최대 힙과 최소 힙의 크기가 같다면 최대 힙에 추가
    if len(max_heap) == len(min_heap):
        # 파이썬의 heapq는 최소 힙이므로, 부호를 바꿔서 최대 힙처럼 사용
        heapq.heappush(max_heap, -num)
    # 최대 힙의 크기가 더 크다면 최소 힙에 추가
    else:
        heapq.heappush(min_heap, num)

    # 2. 재조정: 값 정렬 규칙 확인 및 조정
    # 두 힙이 비어있지 않고, 최대 힙의 최댓값이 최소 힙의 최솟값보다 크다면
    # (주의: max_heap[0]은 음수이므로 -를 붙여 원래 값으로 비교)
    if min_heap and -max_heap[0] > min_heap[0]:
        # 두 힙의 top 원소를 교환
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)

    # 3. 중간값 말하기: 최대 힙의 top이 항상 중간값
    # (주의: max_heap[0]은 음수이므로 -를 붙여 원래 값으로 출력)
    print(-max_heap[0])