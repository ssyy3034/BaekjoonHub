num = int(input())
hansu = 99
if num < 100:
    hansu = num
for i in range(100,num+1):
    calc = str(i)
    front =  int(calc[2]) - int(calc[1])
    rear = int(calc[1]) - int(calc[0])
    if front == rear:
        hansu +=1

print(hansu)
