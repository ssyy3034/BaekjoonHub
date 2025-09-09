arr = [1, 2, 3, 4]

result = []
def combi(idx, start, r):
    global arr
    global result

    if idx == r:
        print(result)
        return

    for i in range(start, len(arr)):
        result.append(arr[i])
        combi(idx+1, i+1, r)
        result.pop()

combi(0, 0, 2)