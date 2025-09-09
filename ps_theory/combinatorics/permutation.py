arr = [1, 2, 3, 4]

pm = []
check = [0] * len(arr)

def recur(idx):
    global pm
    global check
    global arr

    if idx == len(arr):
        print(pm)
        return

    for i in range(len(arr)):
        if check[i] == 0:
            check[i] = 1
            pm.append(arr[i])
            recur(idx + 1)
            pm.pop()
            check[i] = 0    

recur(0)