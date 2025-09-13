import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 포켓몬의 개수, M: 맞춰야 하는 문제의 개수
n, m = map(int, input().split())

# 1. 이름 -> 번호 딕셔너리
name_to_num = {}
# 2. 번호 -> 이름 딕셔너리
num_to_name = {}

for i in range(1, n + 1):
    name = input().rstrip()
    # 각 딕셔너리에 정보 저장
    name_to_num[name] = i
    num_to_name[i] = name

# M개의 문제 풀이
for _ in range(m):
    query = input().rstrip()

    # isdigit()은 문자열이 숫자로만 이루어져 있는지 확인하는 함수
    if query.isdigit():
        # 입력이 숫자면 번호 -> 이름 딕셔너리에서 찾기
        print(num_to_name[int(query)])
    else:
        # 입력이 문자면 이름 -> 번호 딕셔너리에서 찾기
        print(name_to_num[query])