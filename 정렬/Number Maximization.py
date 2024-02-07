import sys

numList = list(map(int, sys.stdin.readline().strip()))  

numList.sort(reverse=True)

for i in range(len(numList)):
  print(numList[i], end='')