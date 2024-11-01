import sys

numList = list(map(int, sys.stdin.readline().strip().split()))

sortedNumList = sorted(numList, reverse=True)

if sortedNumList[0] < (sortedNumList[1] + sortedNumList[2]):
  print(sum(sortedNumList))
else:
  print((sortedNumList[1]+sortedNumList[2])*2 - 1)