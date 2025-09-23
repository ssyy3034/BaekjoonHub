from collections import deque
import sys

# 재귀 제한을 늘릴 필요가 없습니다. BFS는 큐를 사용하기 때문입니다.
# sys.setrecursionlimit(10**6) 

# 입력 받기
n, k = map(int, input().split())

# 방문 여부와 해당 지점까지 걸린 시간을 저장할 리스트
# 최대 위치가 100,000이므로 크기를 100001로 설정합니다.
# 처음에는 모두 방문하지 않았다는 의미로 0으로 채웁니다.
visited = [0] * 100001

def bfs():
    # 큐(Queue) 생성
    q = deque()
    # 시작점 n을 큐에 추가
    q.append(n)
    
    # 큐가 비어있지 않은 동안 반복
    while q:
        # 큐에서 현재 위치 x를 꺼냄
        x = q.popleft()
        
        # 현재 위치가 동생의 위치와 같다면
        if x == k:
            # 시작점은 0초이므로, visited[x]가 바로 최단 시간입니다.
            print(visited[x])
            # 탐색 종료
            return
        
        # 세 가지 이동 방법을 모두 확인합니다.
        # (x-1, x+1, 2*x)
        for next_x in (x - 1, x + 1, x * 2):
            # 다음 위치가 유효한 범위(0~100000) 안에 있고,
            # 아직 방문하지 않은 곳이라면
            if 0 <= next_x <= 100000 and not visited[next_x]:
                # 이전 시간(visited[x])에 1초를 더해 다음 위치의 시간을 기록
                visited[next_x] = visited[x] + 1
                # 다음 탐색을 위해 큐에 추가
                q.append(next_x)

# n이 k보다 크거나 같은 경우는 -1로만 이동 가능합니다.
if n >= k:
    print(n - k)
# 그 외의 경우는 BFS를 실행합니다.
else:
    bfs()