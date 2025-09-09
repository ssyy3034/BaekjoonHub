
N = input()
new_num = 0
count = 0
N = str(f"{int(N):02d}")
num1 = int(N[0])
num2 = int(N[1])
if int(N) == 0:
    count += 1
while new_num != int(N):
    new_num = num2*10+((num1+num2)%10)
    count +=1
    if N == 0:
        break
    if new_num < 10 :
        num2 = num1
        num1 = 0
    else:
        num1 = int(str(new_num)[0])
        num2 = int(str(new_num)[1])
print(count)

