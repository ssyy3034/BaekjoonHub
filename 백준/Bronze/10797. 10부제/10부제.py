N = int(input())
N_list = list(map(int,input().split()))
count = 0
for number in N_list:
    if number == N:
        count+=1
print(count)