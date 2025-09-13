import sys

# 테스트 케이스의 수 T
t = int(sys.stdin.readline())

for _ in range(t):
    # 괄호 문자열 입력
    ps = sys.stdin.readline().rstrip()
    stack = []
    is_vps = True  # 올바른 괄호 문자열인지 판별하는 변수

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # 닫는 괄호인데 스택이 비어있으면 NO
            if not stack:
                is_vps = False
                break
            # 비어있지 않으면 하나 pop
            stack.pop()

    # 루프가 끝난 후 스택에 괄호가 남아있으면 NO
    if stack:
        is_vps = False

    # 최종 결과 출력
    if is_vps:
        print("YES")
    else:
        print("NO")