a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))
arr = [0] * 10

for r in result:
    arr[int(r)] += 1  

for x in arr:
    print(x)
