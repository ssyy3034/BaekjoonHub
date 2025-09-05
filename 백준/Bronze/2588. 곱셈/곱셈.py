num1 = int(input())
num2 = input()

a, b, c = int(num2[0]), int(num2[1]), int(num2[2])

process_A = num1*c
process_B = num1*b
process_C = num1*a

d = process_A + process_B*10 + process_C*100
print(process_A)
print(process_B)
print(process_C)
print(d)


