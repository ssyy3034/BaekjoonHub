import sys
input = sys.stdin.readline
N,M = map(int,input().split())

password = {}
for _ in range(N):
    pwd = input().rstrip().split(" ")
    password[pwd[0]] = pwd[1]
for _ in range(M):
    find = input().rstrip()
    print(password[find])

