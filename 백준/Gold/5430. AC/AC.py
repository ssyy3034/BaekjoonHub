import sys
from collections import deque

# 테스트 케이스의 개수 입력
test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    # 실행할 함수(명령어)
    commands = sys.stdin.readline().rstrip()
    # 배열에 들어있는 수의 개수 (실제로는 사용하지 않아도 무방)
    n = int(sys.stdin.readline())
    # 배열 입력받기
    # "[1,2,3,4]" 형태의 문자열을 파싱하여 deque로 만듦
    input_str = sys.stdin.readline().rstrip()

    # n이 0일 경우, 빈 배열이 들어오므로 예외 처리
    if n == 0:
        q = deque()
    else:
        # [1:-1]로 대괄호 제거 후 ',' 기준으로 split하여 deque 생성
        q = deque(input_str[1:-1].split(','))

    # 💡 핵심: 뒤집혔는지 상태만 저장하는 플래그
    is_reversed = False
    # 에러 발생 여부를 저장하는 플래그
    error_flag = False

    # 명령어 순회
    for cmd in commands:
        if cmd == 'R':
            # 실제로 뒤집지 않고, 플래그만 변경 (O(1) 연산)
            is_reversed = not is_reversed
        elif cmd == 'D':
            # 덱이 비어있으면 에러 처리
            if not q:
                error_flag = True
                break

            # 플래그 상태에 따라 pop 방향 결정 (O(1) 연산)
            if is_reversed:
                q.pop()  # 뒤집힌 상태에서는 뒤에서 제거
            else:
                q.popleft()  # 정방향 상태에서는 앞에서 제거

    # 최종 결과 출력
    if error_flag:
        print("error")
    else:
        # 모든 명령 후, 만약 최종 상태가 뒤집힌 상태라면 그때 딱 한번만 뒤집어줌
        if is_reversed:
            q.reverse()

        # "[1,2,3]" 형태의 문자열로 만들어 출력
        print("[" + ",".join(q) + "]")