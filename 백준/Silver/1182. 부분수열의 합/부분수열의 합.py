N,S = map(int,input().split())
num_list = list(map(int,input().split()))

count = 0
test = []
def find(idx,num,used):
    global count

    if idx == N:
        if num == S and used != 0:
            count +=1
        return

    find(idx+1,num+num_list[idx],used+1)
    find(idx+1,num,used)

find(0,0,0)
print(count)




