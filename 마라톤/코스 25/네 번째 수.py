import sys

numList = list(map(int, sys.stdin.readline().strip().split()))
sortedNumList = sorted(numList)

difference = sortedNumList[1] - sortedNumList[0]

if difference == (sortedNumList[2] - sortedNumList[1]):
  print(sortedNumList[2]+difference)
elif difference > (sortedNumList[2] - sortedNumList[1]):
  print(sortedNumList[0] + (sortedNumList[2] - sortedNumList[1]))
else:
  print(sortedNumList[1] + difference)