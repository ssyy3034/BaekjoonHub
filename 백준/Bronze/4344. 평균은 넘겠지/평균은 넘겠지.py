tc = int(input())
for _ in range(tc):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    avg = sum(scores) / n
    good = sum(1 for s in scores if s > avg)
    print(f"{good / n * 100:.3f}%")
