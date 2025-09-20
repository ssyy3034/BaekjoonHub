def recur(depth):
    if depth == m:
        print(*arr)
        return

    for j in range(n):

        arr.append(n_list[j])
        recur(depth+1)
        arr.pop()

arr = []

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()


recur(0)