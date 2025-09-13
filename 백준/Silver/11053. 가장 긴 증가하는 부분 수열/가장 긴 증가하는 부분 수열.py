import sys
from bisect import bisect_left

# 입력 받기
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# LIS를 만들기 위한 최적의 값을 저장하는 리스트
lis_array = []

for num in A:
    # lis_array가 비어있거나, 현재 숫자가 lis_array의 마지막 값보다 크면
    # lis_array에 현재 숫자를 추가하여 LIS 길이를 1 늘립니다.
    if not lis_array or lis_array[-1] < num:
        lis_array.append(num)
    else:
        # 그렇지 않으면, lis_array에서 현재 숫자(num)보다 크거나 같은 값 중
        # 가장 왼쪽에 있는 값(Lower Bound)의 위치를 찾습니다.
        # 이 과정을 bisect_left가 O(log N)으로 수행해줍니다.
        idx = bisect_left(lis_array, num)
        
        # 해당 위치의 값을 현재 숫자로 교체합니다.
        # 길이는 변하지 않지만, 더 작은 값으로 대체되어
        # 이후에 더 긴 수열을 만들 가능성을 높여줍니다.
        lis_array[idx] = num

# lis_array의 길이가 최종적인 가장 긴 증가하는 부분 수열의 길이입니다.
print(len(lis_array))