import sys
data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

t = next(it)
out = []
for _ in range(t):
    n = next(it)
    iv_of_doc = [0]*(n+1)
    for _ in range(n):
        d = next(it); m = next(it)
        iv_of_doc[d] = m

    cnt, mn = 0, 10**9
    for d in range(1, n+1):
        iv = iv_of_doc[d]
        if iv < mn:
            cnt += 1
            mn = iv
    out.append(str(cnt))

sys.stdout.write("\n".join(out))
