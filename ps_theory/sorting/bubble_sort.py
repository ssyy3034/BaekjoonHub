def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 마지막 i개 원소는 이미 정렬된 상태라 검사할 필요 없음
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [5, 3, 8, 4, 2]
print(bubble_sort(nums))  # [2, 3, 4, 5, 8]