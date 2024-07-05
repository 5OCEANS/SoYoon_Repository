import sys

N = int(sys.stdin.readline().strip())

res = int(sys.stdin.readline().strip())

for i in range(N-1):
  num = int(sys.stdin.readline().strip())

  res += (num - 1)

print(res)

