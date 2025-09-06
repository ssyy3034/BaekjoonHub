import sys
input = sys.stdin.readline
#
n,r,c= map(int,input().split())
quadrant_count = 0


def zFind(n,x,y):
    global quadrant_count
    if n == 0:
        print(quadrant_count)
        return
    size = 2**n
    half_size = size // 2

    if r < x+half_size and c < y+half_size:
        zFind(n-1,x,y)
    elif r < x+half_size and c >= y+half_size:
        quadrant_count += half_size*half_size*1
        zFind(n-1,x,y+half_size)
    elif r >= x+half_size and c < y+half_size:
        quadrant_count += half_size*half_size*2
        zFind(n-1,x+half_size,y)
    elif r >= x+half_size and c >= y+half_size:
        quadrant_count += half_size*half_size*3
        zFind(n-1,x+half_size,y+half_size)
zFind(n, 0, 0)


