import sys

T = int(sys.stdin.readline())

for i in range(T):
  s, p = sys.stdin.readline().strip().split()

  ans = 0

  cnt = s.count(p)

  left = len(s) - len(p) * cnt

  ans = cnt + left

  print(ans)
