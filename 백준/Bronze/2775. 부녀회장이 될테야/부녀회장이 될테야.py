import sys

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호

    # 0층부터 k층까지, 1호부터 n호까지의 인원을 저장할 2차원 리스트
    # 층은 0~k, 호수는 1~n이므로 (k+1) x (n+1) 크기로 만듭니다.
    apt = [[0] * (n + 1) for _ in range(k + 1)]

    # 1. 베이스 케이스: 0층 초기화
    for i in range(1, n + 1):
        apt[0][i] = i

    # 2. 점화식을 이용해 1층부터 k층까지 계산
    for i in range(1, k + 1):  # 1층부터 k층까지
        for j in range(1, n + 1):  # 1호부터 n호까지
            # k층 n호 = (k-1)층 n호의 사람 수 + k층 (n-1)호의 사람 수
            apt[i][j] = apt[i - 1][j] + apt[i][j - 1]

    # k층 n호의 사람 수 출력
    print(apt[k][n])