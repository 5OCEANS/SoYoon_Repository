import sys

N = int(sys.stdin.readline())

for i in range(N):
  stringList = list(sys.stdin.readline().strip().split())
  
  stringList.append(stringList.pop(0))
  stringList.append(stringList.pop(0))
  
  for i in range(len(stringList)):
    print(stringList[i], end = ' ')

  print()