import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards,int(input()))
all_hap = 0
if len(cards) != 1:
    while True:
        if len(cards) == 2:
            all_hap += cards[0] + cards[1]
            break
        hap = 0
        hap += heapq.heappop(cards)
        hap += heapq.heappop(cards)
        all_hap += hap
        heapq.heappush(cards, hap)
print(all_hap)




