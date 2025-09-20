a = int(input())

n_list = list(map(int,input().split()))

prefix = [-999999999 for i in range(a+1)]
for i in range(a):

    prefix[i+1] = max(prefix[i] + n_list[i],n_list[i])
print(max(prefix))

