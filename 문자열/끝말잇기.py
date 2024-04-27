import sys

N = int(sys.stdin.readline())

stringList = sys.stdin.readline().strip().split()
stringstr = stringList[0][0]

for i in stringList:
  if i[0] == stringstr:
    continue
  else:
    print(0)
    break
else:
  print(1)