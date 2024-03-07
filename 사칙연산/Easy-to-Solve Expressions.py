import sys

numList = list(map(int, sys.stdin.readline().split()))
maxNum = max(numList)
numList.remove(maxNum)
middleNum = max(numList)
numList.remove(middleNum)
minNum = max(numList)

if maxNum == middleNum + minNum:
  print(1)
elif maxNum == middleNum * minNum:
  print(2)
else:
  print(3)