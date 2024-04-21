import sys

n = int(sys.stdin.readline())

for i in range(n):
  p = int(sys.stdin.readline())

  cList = []
  nameList = []

  for j in range(p):
    C, name = sys.stdin.readline().split()
    cList.append(int(C))
    nameList.append(name)

  print(nameList[cList.index(max(cList))])