import sys
input = sys.stdin.readline
N = int(input())
stk = []

for i in range(N):
    command = input().rstrip().split(" ")
    if command[0] == "push":
        stk.append(command[1])
    elif command[0] == "top":
        if not stk:
            print(-1)
        else:
            print(stk[-1])
    elif command[0] == "size":
        print(len(stk))
    elif command[0] == "empty":
        if not stk:
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if not stk:
            print(-1)
        else:
            print(stk.pop())