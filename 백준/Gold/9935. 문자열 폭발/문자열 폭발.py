import sys
sentence = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

bomb_len = len(bomb)

answer = []
#answer에 담아가면서 만약 -bomb_len으로 뒤에서부터 슬라이싱 했을때 bomb이면 answer.pop()

for char in sentence:
    answer.append(char)
    if ''.join(answer[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            answer.pop()
if len(answer) == 0:
    print("FRULA")
else:
    print(''.join(answer))

