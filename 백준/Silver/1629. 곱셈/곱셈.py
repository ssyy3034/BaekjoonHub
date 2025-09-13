A,B,C = map(int,input().split())

'''
a를 b번 곱한수  = (a*b)%12 = (a*b)//12 + 나머지 = a//12 *b//12
'''
def power(A,B,C):
    if B == 1:
        return A%C
    half = power(A,B//2,C)
    if B%2 == 0:
        return (half*half)%C
    else:
        return (half*half*A)%C
print(power(A,B,C))