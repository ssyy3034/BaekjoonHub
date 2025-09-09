import sys
input = sys.stdin.readline

self_num_list = [False]*10001

for i in range(10001):
    d = i
    for digit in str(d):
        d += int(digit)

    if d<= 10000:
        self_num_list[d] = True
for i in range(10001):
    if not self_num_list[i]:
        print(i)


