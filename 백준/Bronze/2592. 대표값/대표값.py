n_list = [0]*100
n1_list = []
for i in range(10):
    n = int(input())
    n1_list.append(n)
    idx = n//10
    n_list[idx] += 1
print(sum(n1_list)//len(n1_list))
print(n_list.index(max(n_list))*10)