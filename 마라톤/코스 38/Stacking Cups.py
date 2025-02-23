import sys

N = int(sys.stdin.readline().strip())
cupList = list()
for i in range(N):
  stringList = list(sys.stdin.readline().strip().split())
  if stringList[0].isdigit():
    cupList.append((stringList[1], int(stringList[0])//2))
  else:
    cupList.append((stringList[0], int(stringList[1])))
cupList.sort(key=lambda x:(x[1]))
for i in range(N):
  print(cupList[i][0])