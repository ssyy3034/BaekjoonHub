'''
나무의 수 n개 받은 다음, 가져갈 높이 M으로 저장
list로 나무 길이들 받고, max를 나무 최대 높이로 설정(그 이상은 자를필요 x)
리스트 한번 정렬하고, max+ low(가장 낮은 높이) //2 로 미드 잡음
미드에서 검사 한번 하고,
여기서 검사하는 로직은 tree를 순회하며 mid를 빼서 높이 합 구함
미드 검사 후 미드보다 값이 크면 mid = low+1
아니면 mid = max-1

'''
N,M = map(int,input().split())
trees = list(map(int,input().split()))

trees.sort()
high = max(trees)
low = 0
max_cut = 0
while low <= high:
    mid = (low + high) // 2
    tree_high = 0
    for tree in trees:
          # 자르는 높이
        if tree > mid:
            tree_high += tree - mid
    if tree_high >= M:
        if mid >= max_cut:
            max_cut = mid
        low = mid + 1
    else:
        high = mid - 1
print(max_cut)

