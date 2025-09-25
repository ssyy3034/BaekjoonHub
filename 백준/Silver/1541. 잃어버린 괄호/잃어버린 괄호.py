sent = input()
sentence = []
num = ''

for ch in sent:
    if ch.isdigit():
        num +=ch
    else:
        sentence.append(num)
        num = ''
        sentence.append(ch)
if num:
    sentence.append(num)
hap = int(sentence[0])

if not '+' in sentence :
    for s in range(1,len(sentence)):
        if sentence[s].isdigit():
            hap -= int(sentence[s])
    print(hap)
    exit(0)

flag = 0
for i in range(1,len(sentence)):
    num = sentence[i]
    if num.isdigit():
        if flag:
            hap -= int(num)
        else:
            hap += int(num)
    elif sentence[i] == '+':
       continue
    elif sentence[i] == '-':
       flag = 1
print(hap)
