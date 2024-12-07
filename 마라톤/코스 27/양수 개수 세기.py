import sys

numList = map(int,sys.stdin.readline().strip().split())
ans = 0
for num in numList:
  if num > 0:
    ans += 1
print(ans)