a, b = map(int,input().split())
num_list =list(map(int,input().split()))
answer = []
for i in range(a):
    num = num_list[i]
    if num < b:
        answer.append(num)
print(*answer)

