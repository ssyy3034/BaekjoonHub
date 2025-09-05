
def hanoi(n,x,y,z):
    if n == 1:
        print(x,y)
        return

    hanoi(n -1,x,z,y)
    print(x,y)
    hanoi(n - 1,z,y,x)
N = int(input())
print(2**N-1)
if N<=20:
    hanoi(N,1,3,2)
