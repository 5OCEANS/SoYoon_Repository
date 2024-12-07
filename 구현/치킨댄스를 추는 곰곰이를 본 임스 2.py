import sys

N = int(sys.stdin.readline())
ans = 0
for i in range(N):
  n = int(list(sys.stdin.readline().strip().split('-'))[1])
  if n <= 90:
    ans += 1
print(ans)