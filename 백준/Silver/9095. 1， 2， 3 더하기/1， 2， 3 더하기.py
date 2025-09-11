case = [0]*12

case[1] = 1
case[2] = 2
case[3] = 4
for i in range(4, 12):
    case[i] = case[i-1] + case[i-2] +case[i-3]

n = int(input())

for _ in range(n):
    number = int(input())
    print(case[number])