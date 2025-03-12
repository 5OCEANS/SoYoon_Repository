import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ans = m
for _ in range(n):
  i, j = map(int, sys.stdin.readline().strip().split())
  m += (i-j)
  if m < 0:
    ans = 0
    break
  ans = max(ans, m)
print(ans)