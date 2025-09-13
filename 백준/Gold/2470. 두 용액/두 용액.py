N = int(input())
sol = list(map(int, input().split()))

sol.sort()

low = 0
high = len(sol) - 1

# 결과 저장을 위한 변수들
# result는 두 용액의 합의 절댓값 중 최솟값을 저장
result = float('inf') 
# answer는 result를 만들었던 두 용액을 저장
answer = [0, 0]

while low < high:
    # sol1, sol2 대신 인덱스로 직접 합을 계산
    hap = sol[low] + sol[high]

    # 현재 합의 절댓값이 기존의 최솟값보다 작으면 갱신
    if abs(hap) < result:
        result = abs(hap)
        answer[0] = sol[low]
        answer[1] = sol[high]

    # 합이 0이면 더는 탐색할 필요가 없으므로 종료
    if hap == 0:
        break
    # 합이 0보다 작으면 더 큰 수가 필요하므로 low 포인터를 오른쪽으로 이동
    elif hap < 0:
        low += 1
    # 합이 0보다 크면 더 작은 수가 필요하므로 high 포인터를 왼쪽으로 이동
    else:
        high -= 1

print(*answer)