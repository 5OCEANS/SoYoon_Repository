import sys

N = int(sys.stdin.readline())
numList = []

for i in range(N):
  num = int(sys.stdin.readline())
  numList.append(num)

numList.sort()

for i in range(N):
  print(numList[i])