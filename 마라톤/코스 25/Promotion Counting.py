import sys

L = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(4))
ans = [0, 0, 0]

bef, aft = 0, 0
for i in range(4):
  bef += L[i][0]
  aft += L[i][1]

if aft > bef:
  L[0][0] += (aft - bef)

for i in range(3, -1, -1):
  if L[i][1] > L[i][0]:
    ans[i-1] = L[i][1] - L[i][0]
    L[i-1][1] += (L[i][1] - L[i][0])

for a in ans:
  print(a)