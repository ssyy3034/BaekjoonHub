import heapq
import sys

n = int(sys.stdin.readline())
lines = []
for _ in range(n):
    h,o = map(int, sys.stdin.readline().split())
    lines.append(sorted((h,o)))

d = int(sys.stdin.readline())

possible_lines =[line for line in lines if line[1]-line[0] <=d]

possible_lines.sort(key=lambda x:x[1])

priority_queue =[]
max_count = 0
for start,end in possible_lines:

    railroad_start = end -d
    heapq.heappush(priority_queue,start)

    while priority_queue and priority_queue[0] < railroad_start:
        heapq.heappop(priority_queue)

    max_count = max(max_count,len(priority_queue))

print(max_count)



