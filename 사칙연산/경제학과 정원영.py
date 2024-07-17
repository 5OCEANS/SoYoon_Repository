import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  emptyString = sys.stdin.readline().strip()
  N, M = map(int,sys.stdin.readline().strip().split())

  Nlist = list(map(int, sys.stdin.readline().strip().split()))
  Mlist = list(map(int, sys.stdin.readline().strip().split()))

  ans = 0

  NAvg = sum(Nlist) / N
  MAvg = sum(Mlist) / M

  for j in range(len(Nlist)):
    if Nlist[j] < NAvg and Nlist[j] > MAvg:
      ans += 1

  print(ans)