tc = int(input())
T_list =[]
P_list = []
for i in range(tc):
    T,P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)

max_sum = 0
def time_check(idx,hap):
    global max_sum
    if idx >= len(T_list):
        max_sum = max(max_sum, hap)
        return


    if idx+T_list[idx] <= tc:
        time_check(idx + T_list[idx], hap + P_list[idx])
    time_check(idx+1,hap)
time_check(0,0)
print(max_sum)