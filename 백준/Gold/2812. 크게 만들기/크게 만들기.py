import sys

# n: 숫자의 전체 길이, k: 제거할 숫자의 개수
n, k = map(int, sys.stdin.readline().split())
# 숫자를 입력받아 각 자리를 정수 리스트로 변환
number_str = sys.stdin.readline().strip()
number = [int(char) for char in number_str]

stack = []
# 제거 횟수를 저장할 변수
k_removals = k

# 1. 숫자를 앞에서부터 하나씩 순회
for num in number:
    # 2. 스택이 비어있지 않고, 제거 횟수가 남아있으며, 
    #    스택의 맨 위 숫자가 현재 숫자보다 작으면 pop
    while stack and k_removals > 0 and stack[-1] < num:
        stack.pop()
        k_removals -= 1

    # 3. 현재 숫자를 스택에 push
    stack.append(num)

# 4. 모든 숫자를 다 넣었는데 k가 아직 남아있다면,
#    (예: 98765처럼 내림차순이라 pop이 한 번도 안 일어난 경우)
#    뒤에서부터 남은 k만큼 자른다.
if k_removals > 0:
    result = stack[:-k_removals]
else:
    result = stack

# 최종 결과를 문자열로 합쳐서 출력
print("".join(map(str, result)))