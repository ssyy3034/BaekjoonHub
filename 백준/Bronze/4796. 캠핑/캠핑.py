case_count = 0
while True:
    L,P,V = map(int,input().split())
    if L == P == V == 0:
        exit(0)
    time = 0
    N = V//P
    remain = V-(N*P)
    if remain >=L:
        time = L
    else:
        time = remain

    case_count+=1
    print(f'Case {case_count}: {N*L+time}')
