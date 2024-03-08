import sys

N, M = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(N):
  mlist = list(sys.stdin.readline())
  oCnt = 0
  for j in mlist:
    if j == 'O':
      oCnt += 1
  
  if oCnt >= M//2 + 1:
    cnt += 1

print(cnt)