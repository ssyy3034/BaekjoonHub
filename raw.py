def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>= 0 and key <arr[j]: # j==0이면 탐색 끝, key > arr[j] 면 위치 찾아서 탐색 끝
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
random_num_list = [1,6,7,4,3,2,6,8,10]
print(insert_sort(random_num_list))
