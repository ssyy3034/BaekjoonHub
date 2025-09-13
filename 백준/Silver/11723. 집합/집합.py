import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 연산의 수 M 입력
m = int(input())

# 집합 S를 나타낼 정수 변수 (초기값은 공집합)
s = 0

for _ in range(m):
    # 입력된 명령어 처리
    command = input().rstrip().split()
    op = command[0]

    if op == "add":
        x = int(command[1])
        # x번째 비트를 1로 만든다 (OR 연산)
        # (x-1)을 하는 이유는 숫자는 1-20, 비트 위치는 0-19이기 때문
        s |= (1 << (x - 1))
    
    elif op == "remove":
        x = int(command[1])
        # x번째 비트만 0으로 만든다 (AND와 NOT 연산)
        s &= ~(1 << (x - 1))

    elif op == "check":
        x = int(command[1])
        # x번째 비트가 1인지 확인 (AND 연산)
        if s & (1 << (x - 1)):
            print(1)
        else:
            print(0)

    elif op == "toggle":
        x = int(command[1])
        # x번째 비트를 반전시킨다 (XOR 연산)
        s ^= (1 << (x - 1))

    elif op == "all":
        # 20개의 비트를 모두 1로 채운다
        # (1 << 20)은 21번째 비트가 1인 수이므로, -1을 하면 하위 20개 비트가 모두 1이 됨
        s = (1 << 20) - 1

    elif op == "empty":
        # 공집합으로 만든다
        s = 0