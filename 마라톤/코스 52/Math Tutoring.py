import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  numList[0] = numList[0]-1
  numList.pop()
  for j in range(len(numList)-1, 0, -1):
    numList[j] = numList[j] * (len(numList)-j)

  print('Case %d:' %(i+1), *numList)