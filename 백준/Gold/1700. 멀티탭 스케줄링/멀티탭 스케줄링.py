import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    schedule = list(map(int, sys.stdin.readline().split()))

    multitap = []
    unplugs = 0

    for i in range(k):
        item = schedule[i]

        if item in multitap:
            continue

        if len(multitap) < n:
            multitap.append(item)
            continue

        unplugs += 1
        farthest_use_item = -1
        farthest_use_index = -1

        for plugged_item in multitap:
            try:
                future_index = schedule[i+1:].index(plugged_item)
                if future_index > farthest_use_index:
                    farthest_use_index = future_index
                    farthest_use_item = plugged_item
            except ValueError:
                farthest_use_item = plugged_item
                break

        multitap.remove(farthest_use_item)
        multitap.append(item)

    print(unplugs)

solve()