import sys

n = int(sys.stdin.readline().strip())
ans = 0
for i in range(n):
  d = int(sys.stdin.readline())
  if d % 2 == 1:
    ans += 1
print(ans)