
n = int(input())
for i in range(n):
    total = i + sum(int(d) for d in str(i))
    if total == n:
        print(i)
        break
else:
    print(0)