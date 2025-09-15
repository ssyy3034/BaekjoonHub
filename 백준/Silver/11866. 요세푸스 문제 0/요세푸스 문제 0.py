N,K = map(int,input().split())
result = []
n_list = [i for i in range(1, N + 1)]
recent = 0
while len(n_list) > 0:
    recent = (recent+(K-1))%len(n_list)
    result.append(n_list.pop(recent))

print("<" + ", ".join(map(str,result)) + ">")
