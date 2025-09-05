N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
num_list.sort()
for j in range(N):
    print(num_list[j])