import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 듣도 못한 사람의 명단을 Set에 저장 (탐색 속도 O(1))
not_hear = set()
for _ in range(n):
    not_hear.add(input().strip())

who = []
# 2. 보도 못한 사람을 한 명씩 확인하면서 Set에 있는지 검사
for _ in range(m):
    person = input().strip()
    if person in not_hear:
        who.append(person)

# 3. 결과를 사전순으로 정렬
who.sort()

# 4. 결과 출력
print(len(who))
for person in who:
    print(person)