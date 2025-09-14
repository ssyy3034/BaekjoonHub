'''
사냥꾼은 사대에서 L만큼 사격함.
동물은 각자 위치가 있고, 동물 리스트를 순회하며 사대 찾기?

'''
M,N,L = map(int,input().split())

sadae = list(map(int,input().split()))
sadae.sort()

count = 0
for i in range(N):
    x,y = map(int,input().split())

    start = 0
    end = M-1

    while start <= end:
        mid = (start+end)//2
        distance = abs(sadae[mid] - x)+y
        if distance <= L:
            count+=1
            break
        if sadae[mid] < x:
            start = mid+1
        else:
            end = mid-1
print(count)