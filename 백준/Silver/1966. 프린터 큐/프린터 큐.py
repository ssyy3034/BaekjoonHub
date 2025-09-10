from collections import deque

# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    # (중요도, 원래 인덱스)를 저장할 큐
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])

    count = 0
    while queue:
        # 1. 큐에서 문서 하나를 꺼냄
        current_doc = queue.popleft()

        # 2. 나머지 문서 중 중요도가 더 높은 게 있는지 확인
        # any()는 하나라도 참이면 True를 반환
        if any(current_doc[0] < other_doc[0] for other_doc in queue):
            # A) 있다면, 맨 뒤로 보냄
            queue.append(current_doc)
        else:
            # B) 없다면 (자신이 가장 중요하다면)
            count += 1
            # 우리가 찾던 문서라면 정답 출력 후 종료
            if current_doc[1] == M:
                print(count)
                break