import sys

# 입력 처리
input = sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 두 행렬을 곱하는 함수
def multiply(mat1, mat2):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000 # 각 원소를 1000으로 나눈 나머지 저장
    return res

# 분할 정복을 이용한 거듭제곱 함수
def power(mat, b):
    # Base Case: b가 1이면 행렬 mat를 그대로 반환 (단, 1000으로 나눈 나머지)
    if b == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] %= 1000
        return mat
    
    # b를 절반으로 나눠 재귀 호출
    temp = power(mat, b // 2)
    
    # temp를 제곱
    squared_temp = multiply(temp, temp)
    
    # b가 짝수이면 제곱한 결과가 답
    if b % 2 == 0:
        return squared_temp
    # b가 홀수이면 제곱한 결과에 mat를 한 번 더 곱한 결과가 답
    else:
        return multiply(squared_temp, mat)

# 함수 호출 및 결과 출력
result = power(A, B)
for row in result:
    print(*row)