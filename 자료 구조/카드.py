import sys

N = int(sys.stdin.readline())
numDict = dict()

for i in range(N):
  num = int(sys.stdin.readline())
  if num not in numDict:
    numDict[num] = 1
  else:
    numDict[num] += 1

sortedNumDict = sorted(numDict.items(), key= lambda x: (-x[1], x[0]))
print(sortedNumDict[0][0])