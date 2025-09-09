def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i #현재 인덱스 위치임
        for j in range(i+1, n): #현재 인덱스 다음 위치부터 반복
            if arr[j] < arr[min]:
                min = j #arr[j]가 . 작으면 min으로 업데이트 하는걸 반복해서 남은 배열중 최솟값 min에 들어감.
        arr[i], arr[min] = arr[min], arr[i] #값 바꾸기
arr = [1,3,7,90,2,87,31,23,]
print(arr)
selection_sort(arr)
print(arr)