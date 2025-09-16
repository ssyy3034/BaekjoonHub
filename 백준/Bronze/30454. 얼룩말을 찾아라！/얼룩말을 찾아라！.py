import sys

# N: 줄무늬의 수, L: 줄무늬의 길이 (사용하지 않으므로 _ 처리 가능)
n, _ = map(int, sys.stdin.readline().split())

# N개의 줄무늬 중 가장 큰 값을 저장할 변수
max_count = 0
h = 0

# N개의 줄무늬를 하나씩 확인
for _ in range(n):
    # 한 줄의 줄무늬 패턴을 입력받음
    zebra_line = sys.stdin.readline().strip()

    # '0'을 기준으로 문자열을 자른다.
    # 예: "11010111" -> ['11', '', '1', '', '111']
    black_stripes = zebra_line.split('0')

    # 잘린 결과에서 빈 문자열('')이 아닌 것들만 골라 개수를 센다.
    # 즉, 실제 '1' 덩어리의 개수를 센다.
    current_count = 0
    for stripe in black_stripes:
        if stripe != '':  # stripe가 비어있지 않다면 (즉, '1'이 하나라도 있다면)
            current_count += 1

    # 현재 줄의 검은 줄 개수와 지금까지의 최댓값을 비교하여 갱신
    if max_count == current_count:
        h += 1
    elif max_count < current_count:
        h = 1
    max_count = max(max_count, current_count)



# 최종적으로 가장 컸던 값을 출력
print(max_count,h)