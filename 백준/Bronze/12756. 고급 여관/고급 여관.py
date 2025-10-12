p1a,p1b = map(int,input().split())
p2a,p2b = map(int,input().split())

while p1b>1 and p2b>1:
    p1b = p1b-p2a
    p2b = p2b-p1a
if p1b<1 and p2b <1:
    print("DRAW")
    exit(0)
elif p1b >p2b:
    print("PLAYER A")

elif p1b <p2b:
    print("PLAYER B")