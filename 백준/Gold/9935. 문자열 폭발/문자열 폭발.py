import sys

# 입력 문자열과 폭발 문자열의 양쪽 공백 제거
N = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

answer = []
bomb_len = len(bomb)

for char in N:
    answer.append(char)
    # IndexError를 방지하기 위해 스택의 길이가 충분한지 확인
    if len(answer) >= bomb_len:
        # 스택의 마지막 부분이 폭발 문자열과 일치하는지 확인
        if ''.join(answer[-bomb_len:]) == bomb:
            # 일치하면 폭발 문자열만큼 pop
            for _ in range(bomb_len):
                answer.pop()

if not answer:
    print("FRULA")
else:
    print(''.join(answer))