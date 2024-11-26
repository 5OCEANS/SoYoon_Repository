import sys

K, N = map(int, sys.stdin.readline().strip().split())
if N == 1:
  print(-1)
  exit(0)
ans = (K*N) // (N-1)
if (K*N) % (N-1):
  ans += 1
print(ans)