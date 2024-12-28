import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))
ascent = 0
ascentList = []
for i in range(1, len(numList)):
  if numList[i-1] < numList[i]:
    ascent += (numList[i]-numList[i-1])
  else:
    ascentList.append(ascent)
    ascent = 0
ascentList.append(ascent)

if ascentList:
  print(max(ascentList))
else:
  print(0)