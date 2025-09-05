'''
종이 자르는데 가로,세로 있음
자르고 나서 더 큰쪽 선택?
아니면 진짜로 2차원 배열 슬라이스?
'''
W, H = map(int, input().split())
N = int(input())

cutH = [0,H]
cutW = [0,W]

for i in range(N):
    isRowOrColumn , cuts = map(int, input().split())
    if isRowOrColumn == 0:
        cutH.append(cuts)
    else:
        cutW.append(cuts)

cutH.sort()
cutW.sort()

max_h = max(cutH[i+1] - cutH[i] for i in range(len(cutH)-1)) # 가장 큰 세로 길이
max_w = max(cutW[i+1] - cutW[i] for i in range(len(cutW)-1)) # 가장 큰 가로 길이

print(max_h * max_w)


