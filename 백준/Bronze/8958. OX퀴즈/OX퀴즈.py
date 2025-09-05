tc = int(input())
for i in range(tc):
    tc_list = list(input())
    count = 0
    sum = 0
    for t in tc_list:
        if t == 'O':
            count += 1
            sum += count
        if t == 'X':
            count = 0
    print(sum)

