import sys

n = sys.stdin.readline().strip()

def solve():
    stack = []

    for gwalho in n:
        # 1. 여는 괄호는 스택에 추가
        if gwalho in '([':
            stack.append(gwalho)

        # 2. 닫는 괄호 로직 통합
        elif gwalho in ')]':
            temp = 0
            
            # 닫는 괄호에 따라 opener와 multiplier를 설정
            if gwalho == ')':
                opener = '('
                multiplier = 2
            else: # ']'인 경우
                opener = '['
                multiplier = 3
            
            # 스택이 비어있으면 실패
            if not stack:
                return 0

            # --- 여기부터는 괄호 종류와 상관없이 로직이 동일 ---
            while stack:
                top = stack.pop()

                if top == opener:
                    value = temp * multiplier if temp > 0 else multiplier
                    stack.append(value)
                    break # 성공적으로 짝을 찾음
                
                elif isinstance(top, int):
                    temp += top
                
                else: # 짝이 다른 괄호가 나옴
                    return 0
            
            else: # while 루프가 break 없이 끝남 (스택이 모두 비어버림)
                return 0
    
    # 3. 최종 결과 계산
    answer = 0
    for item in stack:
        if not isinstance(item, int): # 괄호가 남아있으면 실패
            return 0
        answer += item
    
    return answer

print(solve())