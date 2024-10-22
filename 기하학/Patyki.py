import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

if a == c and c == b:
  print(2)
else:
  numList = list()
  numList.append(a)
  numList.append(b)
  numList.append(c)
  maxNum = numList.pop(numList.index(max(numList)))
  tmp = pow(numList.pop(), 2) + pow(numList.pop(), 2)

  if pow(maxNum, 2) == tmp:
    print(1)
  else:
    print(0)


numList = list(map(int, input().split()))
numList.sort()
if numList[0] == numList[1] == numList[2]:
  print(2)
elif numList[2] ** 2 == numList[1] ** 2 + numList[0] ** 2:
  print(1)
else:
  print(0)