import sys

T = int(sys.stdin.readline())

for i in range(T):
  stringList = sys.stdin.readline().split()

  for j in range(len(stringList)):
    stringList[j] = stringList[j][::-1]
  
  print(' '.join(stringList))