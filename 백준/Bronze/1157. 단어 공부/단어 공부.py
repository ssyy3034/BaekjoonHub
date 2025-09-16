n = input().upper()
n_list = [0]*26

for ch in n:
    n_list[ord(ch)-65] += 1

most_alpha = 0
result = ''
isNotOnly = False

for i in range(26):
    if n_list[i] > most_alpha:
        most_alpha = n_list[i]
        result = chr(i+65)
        isNotOnly = False
    elif n_list[i] == most_alpha:
        isNotOnly = True

if isNotOnly:
    print("?")
else:
    print(result)

