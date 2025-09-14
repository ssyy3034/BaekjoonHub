import sys
from collections import deque # 1. deque를 import 합니다.

input = sys.stdin.readline

N = int(input())
q = deque() # 2. 리스트 대신 deque로 초기화합니다.
for i in range(N):
    order = input().split()
    if order[0] == "push":
        q.append(int(order[1]))
    elif order[0] == "empty": # 3. empty, front, back, size는 그대로 사용해도 됩니다.
        if not q:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif order[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft()) # 4. q.pop(0) 대신 q.popleft()를 사용합니다.
    elif order[0] == "size":
        print(len(q))