import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
num_list.sort()
sys.stdout.write('\n'.join(map(str, num_list)))
