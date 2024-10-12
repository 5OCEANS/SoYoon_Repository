import sys

N, C = map(int, sys.stdin.readline().strip().split())

numList = list(map(int, sys.stdin.readline().strip().split()))
numDict = dict()

for i in range(N):
  if numList[i] not in numDict:
    numDict[numList[i]] = 1
  else:
    numDict[numList[i]] +=  1

sortednumDict = dict(sorted(numDict.items(), key= lambda x: -x[1]))

for key, val in sortednumDict.items():
  for _ in range(val):    print(key, end = ' ') 
