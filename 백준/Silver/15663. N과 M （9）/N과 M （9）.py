n,m = map(int,input().split())

n_list = list(map(int,input().split()))
n_list.sort()
answer = []
visited = [0 for i in range(n)]
def dfs(count):
    if count == m:
            print(*answer)
            return
    lun = 0
    for i in range(n):
        if not visited[i] and lun !=n_list[i]:
            visited[i] = 1
            answer.append(n_list[i])
            lun = n_list[i]
            dfs(count+1)
            answer.pop()
            visited[i] = 0
dfs(0)
