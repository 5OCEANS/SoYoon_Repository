import sys, math

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))

havetoOddNumCount = math.ceil(N/2)
realOddNumCount = 0
for i in range(N):
  if numList[i] % 2 == 1:
    realOddNumCount += 1

if havetoOddNumCount == realOddNumCount:
  print(1)
else:
  print(0)