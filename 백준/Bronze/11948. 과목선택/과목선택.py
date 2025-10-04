fl = []
sl = []
for i in range(4):
    fl.append(int(input()))
for i in range(2):
    sl.append(int(input()))
fl.sort(reverse=True)
fl.pop()
sl.sort(reverse=True)
sl.pop()
answer = sum(fl)+sl[0]
print(answer)

