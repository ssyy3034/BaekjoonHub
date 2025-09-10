def fizz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
inputs = [input().strip() for _ in range(3)]
find_number = 0
for i in range(3):
    if inputs[i].isdigit():
        num = int(inputs[i])
        find_number = num+(3-i)
        break
print(fizz(int(find_number)))