import sys
sys.setrecursionlimit(10**9)
n = int(input())

def facto(t):
    k = 1
    if t == 0 or t == 1:
        return 1
    return t*facto(t-1)
print(facto(n))