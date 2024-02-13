import sys

N = int(sys.stdin.readline())

for i in range(N):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  numList.sort(reverse=True)

  print(numList[2])