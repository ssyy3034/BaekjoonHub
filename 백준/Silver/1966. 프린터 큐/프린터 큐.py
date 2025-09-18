
from collections import deque

T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    priority = list(map(int, input().split()))

    queue = deque([(p,idx) for idx,p in enumerate(priority)])
    #큐에 넣고 0번은 우선순위,1번은 인덱스로 저장함
    #현재 큐에서 하나를 뽑고, 이 문서의 중요도 검사 ( 0 번 인덱스 비교)
    #만약 중요도가 높은 문서가 뒤에 있다면, 그냥 다시 큐에 넣고 아니라면 그대로 pop하고 카운트 증가. 만약 Pop하면서 문서가 찾는 문서라면 print하고 브레이크
    count = 0
    while queue:
        curr = queue.popleft()

        if any(curr[0] < other[0] for other in queue):
            queue.append(curr)
        else:
            count += 1
            if curr[1] == m:
                print(count)
                break
