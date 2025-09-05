from math import sqrt
tc = int(input())

n = 10000

isPrime = [True]*(n+1)

for i in range(2,int(sqrt(n))+1):
    if isPrime[i]:
        for j in range(i*i,n+1,i):
            isPrime[j] = False

for i in range(tc):
    a= int(input())
    p = a//2
    q = a-p
    while p>=2:
        if isPrime[p] and isPrime[q]:
            print(p,q)
            break
        p -=1
        q = a-p
