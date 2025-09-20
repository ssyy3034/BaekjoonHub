import sys
sys.setrecursionlimit(10**6)
def number_baseball(idx,number):
    c_num = hint[idx][0]
    c_st = hint[idx][1]
    c_ball = hint[idx][2]

    strike = 0
    ball = 0

    _A = c_num // 100
    _B = (c_num - (_A * 100)) // 10
    _C = c_num % 10

    A = number // 100
    B = (number - (A * 100)) // 10
    C = number % 10

    if A == 0 or B == 0 or C == 0:
        return False

    if A == B or A == C or B == C:
        return False

    if A == _A:
        strike += 1
    if B == _B:
        strike += 1
    if C == _C:
        strike += 1

    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1

    if strike == c_st and ball == c_ball:
        return True

    return False

def recur(idx,number):
    global answer

    if idx == n:
        answer += 1
        recur(0,number+1)
        return

    if number == 1000:
        return
    if number_baseball(idx,number):
        recur(idx+1,number)
    else:
        recur(0,number+1)

n = int(input())
answer = 0
hint = [list(map(int,input().split())) for i in range(n)]
recur(0,100)
print(answer)
