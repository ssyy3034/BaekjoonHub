N = int(input())
num = list(map(int, input().split()))
count = 0

for n in num:
    if n < 2:
        continue
    isPrime = True
    for j in range(2, int(n**0.5)+1 ):
        if n%j == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
print(count)