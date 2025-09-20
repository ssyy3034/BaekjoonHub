a,b = map(int,input().split())

n_list = list(map(int,input().split()))

prefix = [0 for i in range(a+1)]
for i in range(a):
    prefix[i+1] = prefix[i] + n_list[i]

answer = []
for k in range(b,a+1):
     answer.append(prefix[k]-prefix[k-b])
print(max(answer))