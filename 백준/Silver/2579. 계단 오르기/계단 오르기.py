import sys

# 계단의 개수 입력
n = int(sys.stdin.readline())

# 각 계단의 점수 입력
# 인덱스를 1부터 시작하게 만들기 위해 맨 앞에 0을 추가해줍니다.
stair = [0] * 301 # 계단이 최대 300개이므로 넉넉하게 공간 확보
for i in range(1, n + 1):
    stair[i] = int(sys.stdin.readline())

# DP 테이블(결과 저장용 리스트) 초기화
dp = [0] * 301

# 계단이 1개 또는 2개일 경우는 점화식을 적용할 수 없으므로 따로 처리합니다.
if n == 1:
    print(stair[1])
else:
    # 초기값 설정
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    
    # 3번째 계단부터 마지막 계단까지 점화식을 적용하여 DP 테이블을 채웁니다.
    for i in range(3, n + 1):
        # 1. (i-2)에서 바로 올라온 경우
        case1 = dp[i-2] + stair[i]
        
        # 2. (i-1)을 밟고 올라온 경우 (그 전은 반드시 i-3)
        case2 = dp[i-3] + stair[i-1] + stair[i]
        
        # 두 경우 중 더 큰 값을 저장
        dp[i] = max(case1, case2)
        
    # 마지막 계단(n)에 도달했을 때의 최댓값이 정답입니다.
    print(dp[n])