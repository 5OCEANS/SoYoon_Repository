# 시간 초과
import sys

N, M = map(int, sys.stdin.readline().strip().split())
treeList = list(map(int, sys.stdin.readline().strip().split()))
maxHeight = max(treeList)

while True:
  try:
    sumTree = 0
    for i in treeList:
      if i >= maxHeight:
        sumTree += (i - maxHeight)
    if sumTree >= M:
      print(maxHeight)
      exit()
    else:
      maxHeight -= 1
  except:
    break



import sys

N, M = map(int, sys.stdin.readline().strip().split())
treeList = list(map(int, sys.stdin.readline().strip().split()))

startHeight = 1
maxHeight = max(treeList)
result = 0

while startHeight <= maxHeight:
  mid = (startHeight + maxHeight) // 2
  sumTree = sum(max(0, tree - mid) for tree in treeList)

  if sumTree >= M:
    result = mid
    startHeight = mid + 1
  else:
    maxHeight = mid - 1

print(result)