# 세 막대의 길이를 입력받아 리스트에 저장
sticks = list(map(int, input().split()))

# 오름차순으로 정렬
sticks.sort()

# 가장 긴 막대가 다른 두 막대의 합보다 작은지 확인
if sticks[2] < sticks[0] + sticks[1]:
    # Case 1: 이미 삼각형이 되는 경우
    print(sum(sticks))
else:
    # Case 2: 삼각형이 안 되는 경우
    # 가장 긴 막대의 길이를 두 막대의 합 - 1로 조절
    max_perimeter = sticks[0] + sticks[1] + (sticks[0] + sticks[1] - 1)
    print(max_perimeter)