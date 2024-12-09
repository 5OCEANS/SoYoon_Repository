import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))
fillSet = set()
ans = 0

for num in numList:
  if num not in fillSet:
    fillSet.add(num)
  else:
    ans += 1

print(ans)