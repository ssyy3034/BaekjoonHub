d1,d2,d3 = map(int,input().split())
ssum = (d1+d2+d3)/2
a = ssum-d3
b = ssum-d2
c = ssum-d1
if a<=0 or b<=0 or c<=0:
    print(-1)
else:
    print(1)
    print(a,b,c)