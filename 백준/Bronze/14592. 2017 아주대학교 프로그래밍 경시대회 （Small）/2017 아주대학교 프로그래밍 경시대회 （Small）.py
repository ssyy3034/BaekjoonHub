n = int(input())
total = []
cnt = []
t = []
for _ in range(n):
    s,c,l = map(int, input().split())
    total.append(s)
    cnt.append(c)
    t.append(l)
    
for i in range(n):
    # 같은 값이 존재하면
    if total.count(total[i]) >= n:
        # 제출 횟수 같은 경우
        if cnt.count(cnt[i]) >= n:
            print(t.index(min(t))+1)
            break
        else:
            print(cnt.index(min(cnt))+1)
            break
    else:
        print(total.index(max(total))+1)
        break