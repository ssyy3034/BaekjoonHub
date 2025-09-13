import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

# (높이, 인덱스)를 저장할 스택
stack = []
# 정답을 저장할 리스트
answer = []

for i in range(N):
    current_height = towers[i]

    # 스택이 비어있지 않고, top의 높이가 현재 높이보다 낮으면 계속 pop
    while stack and stack[-1][0] < current_height:
        stack.pop()

    # while문이 끝난 후 스택의 상태로 정답 결정
    if not stack:  # 스택이 비어있으면 수신할 탑 없음
        answer.append(0)
    else:  # 스택에 남아있는 탑이 수신 탑
        answer.append(stack[-1][1] + 1) # 인덱스는 0부터 시작하므로 +1

    # 현재 탑의 (높이, 인덱스)를 스택에 push
    stack.append((current_height, i))

print(*answer)