import sys

N, X = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
sum_val = 0

b = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N):
  sum_val += b[i]
  if sum_val < a[i]:
    print(-1)
    exit()

print((sum_val - a[N - 1]) // X)