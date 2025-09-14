from collections import deque

N = int(input())
queue = deque(range(1, N + 1)) # 1부터 N까지의 카드를 큐에 넣음

while len(queue) > 1:
    queue.popleft()       # 1. 맨 위의 카드를 버린다.
    queue.append(queue.popleft()) # 2. 그 다음 맨 위의 카드를 뽑아서 맨 아래로 옮긴다.

print(queue[0]) # 마지막에 남은 카드 출력