import sys

while True:
    input_data = list(map(int, sys.stdin.readline().split()))
    n = input_data[0]
    if n == 0:
        break

    h = input_data[1:]

    stack = []
    max_area = 0

    for i,height in enumerate(h):

        start_idx = i
        while stack and stack[-1][1] > height: #height가 맨 위 스택의 높이보다 낮다면

            idx,prev_height = stack.pop() # 현재 인덱스,이전 높이 계산 [스택 탑의 idx,데이터]
            width = i - idx 
            max_area = max(max_area,width * prev_height) #max_area와 prev_height * width한 지금 넓이 계산해서 max 돌림
            start_idx = idx
        stack.append((start_idx, height)) #계산 끝나면 stack에 값 추가
    while stack:
        idx,prev_height = stack.pop() #다 조회하면 스택 돌면서 계속 팝

        width =n-idx 
        max_area = max(max_area,width*prev_height)

    print(max_area)