
N = int(input())
sol = list(map(int, input().split()))

sol.sort()
result = 1000000000000000
'''
0에 가장 가까운 용액을 만들어내는 두 용액을 찾아야 함.
이진탐색이니까.. low,high를 불러와서 더한다?
더한값이 최소인 두 용액의 합 리턴하면 될듯
근데 그러면 그냥 전부 찾는게 되는거 같은데?
차라리 하나를 픽스하고, 그거 짝을 이진탐색 ㄱㄱ
그러면 하나씩 logN 돌아감.
그러면 n'2logN
좋은 방법은 왼쪽 하나, 오른쪽 하나 잡고
합을 계산하면서 최소값 나오면 갱신하고 위치 저장
다시 좁혀가면서 포인터끼리 만나면 끝.
최소값 및 최소값 발생시킨 위치 리턴

그럼 뭐뭐 필요하냐
오른쪽 포인터 하나, 왼쪽 포인터 하나
while 오른쪽 >= 왼쪽일때
sol1,sol2,result,hap 초기화하고
hap = abs(sol[오른쪽]+sol[왼쪽])
if hap >result:
     sol1 = sol[왼쪽]
     sol2 = sol[오른쪽]
     result = hap
if hap == 0:
       리턴
elif hap < 0:
    왼쪽 =  왼쪽 +1
elif hap > -:
    오른쪽 = 오른쪽 +1
이렇게 다 돌리면
    
'''
low =  0
high = len(sol)-1
sol1 = sol[0]
sol2 = sol[-1]
answer = [0]*2
while low < high:
    hap = sol1+sol2
    if abs(hap) < result:
        result = abs(hap)
        answer[0] = sol1
        answer[1] = sol2
    if hap == 0:
        result = hap
        answer[0] = sol1
        answer[1] = sol2
        break
    elif hap < 0:
        low = low +1
        sol1 = sol[low]
    elif hap > 0 :
        high = high -1
        sol2 = sol[high]
print(*answer)

