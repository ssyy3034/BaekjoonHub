import sys
input = sys.stdin.readline

K = int(input())
money = []
for i in range(K):
    n = int(input())
    if n !=0:
        money.append(n)
    else:
        money.pop()
print(sum(money))