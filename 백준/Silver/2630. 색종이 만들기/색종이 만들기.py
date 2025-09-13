import sys

# sys.stdin.readline()을 사용하려면 input()을 대체해줘야 합니다.
# (백준 제출 시에는 이 줄이 없어도 됩니다)
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue_paper = 0
white_paper = 0


def solve(x, y, size):
    global blue_paper, white_paper

    # 1. 현재 영역의 첫 번째 칸 색깔을 기준으로 삼는다.
    color = paper[x][y]

    # 2. 현재 영역을 전부 순회하며 다른 색이 있는지 "검사"부터 한다.
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 만약 다른 색의 종이가 하나라도 발견되면,
            if paper[i][j] != color:
                # 즉시 4분할하여 재귀 호출하고 함수를 종료한다.
                new_size = size // 2
                solve(x, y, new_size)  # 1사분면
                solve(x, y + new_size, new_size)  # 2사분면
                solve(x + new_size, y, new_size)  # 3사분면
                solve(x + new_size, y + new_size, new_size)  # 4사분면
                return  # ★★★ 중요: 분할했으면 현재 함수는 할 일을 다 했으므로 종료!

    # 3. 만약 위쪽 for문이 중단 없이 모두 통과했다면, 이 영역은 모두 같은 색이다.
    # 그 결과에 따라 행동(카운트)한다.
    if color == 1:
        blue_paper += 1
    else:
        white_paper += 1


# 시작
solve(0, 0, N)

print(white_paper)
print(blue_paper)