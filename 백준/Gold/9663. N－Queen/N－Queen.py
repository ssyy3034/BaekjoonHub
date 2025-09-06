# === N-Queen (set 버전, 구조 익히기용) ===
import sys
input = sys.stdin.readline
#
n = int(input().strip())
cols, d1, d2 = set(), set(), set()   # 열, /대각, \대각
ans = 0

def dfs(row):
    global ans
    if row == n:
        ans += 1 #퀸을 전부 배치함
        return
    for col in range(n):
        if col in cols or (row+col) in d1 or (row-col) in d2:
            continue
        cols.add(col);d1.add(row+col);d2.add(row-col)
        dfs(row+1)
        cols.remove(col);d1.remove(row+col);d2.remove(row-col)
dfs(0)
print(ans)
