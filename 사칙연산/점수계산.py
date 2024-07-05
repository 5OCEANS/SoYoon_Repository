import sys

N = int(sys.stdin.readline().strip())

numList = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
last = 0

for i in range(N):
  if numList[i] == 1:
    ans += (last + 1)
    last += 1
  else:
    last = 0

print(ans)