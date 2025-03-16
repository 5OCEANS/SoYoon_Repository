import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
  space = sys.stdin.readline().strip()
  n, q = map(int, sys.stdin.readline().strip().split())
  nList = list(map(int, sys.stdin.readline().strip().split()))

  prefix_sum = [0] * (n+1)
  for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + nList[i]

  for j in range(q):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[j+1] - prefix_sum[i])
  print()