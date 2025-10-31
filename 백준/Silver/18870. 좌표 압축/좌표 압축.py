import sys

N = int(input())
inputList = list(map(int,sys.stdin.readline().rstrip().split()))

sortedList = sorted(list(set(inputList)))
dictList = dict(zip(sortedList,list(range(len(sortedList)))))
printList = []
for x in inputList:
    printList.append(dictList[x])
print(*printList)