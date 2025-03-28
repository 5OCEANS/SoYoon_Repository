import sys

T, N = map(int, sys.stdin.readline().strip().split())
ans = T
dayDic = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4}
for i in range(N):
  d1, h1, d2, h2 = sys.stdin.readline().strip().split()
  h1, h2 = int(h1), int(h2)
  if d1 == d2:
    ans -= (h2-h1)
  else:
    dayDif = dayDic[d2] - dayDic[d1]
    ans -= ((24*dayDif-h1)+h2)
if ans < 0:
  print(0)
elif ans > 48:
  print(-1)
else:
  print(ans)