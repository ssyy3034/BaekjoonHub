n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m_num = int(input())
m_list = list(map(int, input().split()))


answer = []
for m in m_list:
    found = False
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if n_list[mid] == m:
            found = True
            break
        if n_list[mid] < m:
            l = mid+1
        elif n_list[mid] > m:
            r = mid-1
    if found:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)