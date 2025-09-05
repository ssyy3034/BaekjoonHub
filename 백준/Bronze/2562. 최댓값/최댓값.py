max_num =0
max_line = 0
for i in range(9):
    a = int(input())
    if a > max_num:
        max_num = a
        max_line = i+1
print(max_num)
print(max_line)

