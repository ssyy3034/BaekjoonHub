n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))
answer = []
for m in m_list:
    l = 0
    r = n-1
    found = False
    while l <= r:
        mid = (l+r)//2
        if n_list[mid] == m:
            found = True
            break
        elif n_list[mid] < m:
            l = mid+1
        else:
            r = mid-1
    if found:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)
