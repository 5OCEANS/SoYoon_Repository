import sys

numCnt = int(input())

numList = [int(sys.stdin.readline()) for __ in range(numCnt)]

numList.sort()

for i in numList:
  print(i)