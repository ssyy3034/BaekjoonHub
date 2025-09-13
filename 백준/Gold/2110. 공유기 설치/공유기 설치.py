import sys
input = sys.stdin.readline

N,C = map(int,input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
result = 0
start = 1
end = house[-1]

while start <= end:
    mid = (start + end) // 2
    last = house[0]
    count = 1
    for i in range(1,N):
        if house[i] >= last + mid:
            count += 1
            last = house[i]
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid -1
print(result)

