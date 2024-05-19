import sys

N, M = map(int, sys.stdin.readline().strip().split())
stringList = []
testStringList = []

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string)

for i in range(N):
  string = sys.stdin.readline().strip()
  testStringList.append(string)

for i in range(N):
  if testStringList[i][0:2*M:2] != stringList[i] or testStringList[i][1:2*M:2] != stringList[i]:
    print('Not Eyfa')
    break
else:
  print('Eyfa')