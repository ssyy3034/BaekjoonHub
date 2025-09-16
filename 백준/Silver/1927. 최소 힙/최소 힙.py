import heapq
import sys
input = sys.stdin.readline
n=int(input())
q= []
for i in range(n):
    k = int(input())
    if k == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,k)
