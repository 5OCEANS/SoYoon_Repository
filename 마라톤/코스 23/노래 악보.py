import sys

N, Q = map(int, sys.stdin.readline().strip().split())
secondList = list()

for i in range(N):
  second = int(sys.stdin.readline())
  secondList.append(second)

for i in range(Q):
  q = int(sys.stdin.readline())
  for j in range(N):
    if sum(secondList[0:j+1]) >= (q+1):
      print(j+1)
      break