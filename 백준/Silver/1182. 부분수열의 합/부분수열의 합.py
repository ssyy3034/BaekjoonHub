N,S = map(int,input().split())

num_list = list(map(int,input().split()))
count = 0

def calc(idx,hap,used):
    global count

    if idx == N:
        if hap == S and used != 0:
            count += 1
        return

    calc(idx+1,hap+num_list[idx],used+1)

    calc(idx+1,hap,used)
calc(0,0,0)
print(count)

