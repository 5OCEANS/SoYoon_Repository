import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))

cnt = 1
for i in range(n - 1, 0, -1):
  if a[i - 1] < a[i]:
    cnt += 1
  else:
    break

print(n - cnt)