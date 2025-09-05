tc = int(input())
for i in range(tc):
    n,m = input().split()
    m = list(m)
    result = []
    for j in range(len(m)):
        result.append(int(n) * m[j])
    print(''.join(result))
