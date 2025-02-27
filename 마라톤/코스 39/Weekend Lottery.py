import sys

while True:
  N, C, K = map(int, sys.stdin.readline().strip().split())
  if N == 0 and C == 0 and K == 0:
    break
  numList = list()
  for i in range(N):
    num = list(map(int, sys.stdin.readline().strip().split()))
    numList += num
  minCountNum = 10000
  minCountNumList = list()
  for i in range(1, K+1):
    count = numList.count(i)
    if count < minCountNum:
      minCountNum = count
      minCountNumList = list()
      minCountNumList.append(i)
    elif count == minCountNum:
      minCountNumList.append(i)
    else:
      continue
  minCountNumList.sort()
  for i in minCountNumList:
    print(i, end = ' ')
  print()