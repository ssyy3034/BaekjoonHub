num1,num2 = map(str, input().split())

num1_reverse = num1[::-1]
num2_reverse = num2[::-1]
if num1_reverse > num2_reverse:
    print(num1_reverse)
else:
    print(num2_reverse)