import sys

N, M = map(int, sys.stdin.readline().strip().split())
result = 'Yes'

for i in range(M):
  num = int(sys.stdin.readline())
  numList = list(map(int, sys.stdin.readline().split()))
  sortedNumList = sorted(numList, reverse=True)

  if numList == sortedNumList:
    continue
  else:
    result = 'No'

print(result)