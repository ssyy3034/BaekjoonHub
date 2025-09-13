import sys

# 막대기의 수 N
n = int(sys.stdin.readline())
sticks = []

for _ in range(n):
    # int()로 감싸 숫자로 변환하여 저장
    sticks.append(int(sys.stdin.readline()))

# 보이는 막대기의 수 (오른쪽 맨 끝 막대기는 항상 보임)
count = 1
# 가장 오른쪽에 있는 막대기를 초기 가장 높은 막대기로 설정
max_height = sticks[-1]

# 리스트를 거꾸로 탐색 (오른쪽에서 두 번째부터 왼쪽 끝까지)
for i in range(len(sticks) - 2, -1, -1):
    # 현재 막대기가 이전에 본 가장 높은 막대기보다 높다면
    if sticks[i] > max_height:
        count += 1
        # 가장 높은 막대기 높이를 갱신
        max_height = sticks[i]

print(count)