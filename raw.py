n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]
count =0
def recur(x,y):
    global count
    curr = board[x][y]
    if curr == 0:
        count +=1
        return
    if 0<=x+curr<n and 0<=y+curr<n:
        if board[x+curr][y] != -1:
            recur(x+curr,y)
        if board[x][y+curr] !=-1:
            recur(x,y+curr)
    else:
        return
recur(0,0)
print(count)
