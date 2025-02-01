import sys

T = int(sys.stdin.readline())
for _ in range(T):
  blank = sys.stdin.readline()
  cs, e = map(int, sys.stdin.readline().strip().split())
  csIQList = list(map(int, sys.stdin.readline().strip().split()))
  eIQList = list(map(int, sys.stdin.readline().strip().split()))
  avgeIQ = sum(eIQList) / e
  avgcsIQ = sum(csIQList) / cs
  ans = 0
  for i in range(cs):
    if csIQList[i] < avgcsIQ and csIQList[i] > avgeIQ:
      ans += 1
  print(ans)