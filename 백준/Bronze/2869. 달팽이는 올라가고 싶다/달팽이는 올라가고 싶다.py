A,B,V = map(int, input().split())
last_day =  V-A
climb = A-B
days = 0
if last_day%climb == 0:
    days = last_day // climb
else:
    days = (last_day//climb)+1
print(days+1)



