N = int(input())
nlist = set(input().split())
k = int(input())
M= input().split()

for c in M:
    if c in nlist:
        print("1")
    else:
        print("0")