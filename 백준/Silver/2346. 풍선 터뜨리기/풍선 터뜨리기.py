import sys
from collections import deque

n = int(sys.stdin.readline())
papers = list(map(int, sys.stdin.readline().split()))

# 덱을 초기화합니다. (풍선 번호, 종이 안의 값) 형태로 저장합니다.
# 풍선 번호는 1부터 시작하므로 인덱스 i에 1을 더해줍니다.
q = deque([(i + 1, papers[i]) for i in range(n)])

# 결과를 저장할 리스트
result = []

# 덱에 풍선이 남아있는 동안 반복
while q:
    # 1. 맨 앞의 풍선을 터뜨립니다. (popleft)
    balloon_num, paper_val = q.popleft()
    result.append(balloon_num)
    
    # 더 이상 터뜨릴 풍선이 없으면 종료
    if not q:
        break

    # 2. 다음 터뜨릴 풍선을 맨 앞으로 가져옵니다. (rotate)
    if paper_val > 0:
        # 양수이면 오른쪽으로 (paper_val - 1)칸 이동
        q.rotate(-(paper_val - 1))
    else:
        # 음수이면 왼쪽으로 |paper_val|칸 이동
        q.rotate(-paper_val) # paper_val이 음수이므로 -를 붙여 양수로 만듦

# 최종 결과 출력
print(' '.join(map(str, result)))