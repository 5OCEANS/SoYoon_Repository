import sys

T = int(sys.stdin.readline())

for i in range(T):
  sideList = list(map(int, sys.stdin.readline().strip().split()))
  sortedSideList = sorted(sideList)

  if sortedSideList[2] >= (sortedSideList[0] + sortedSideList[1]):
    print('Case #' + str(i+1) + ': invalid!')
    continue

  count = len(set(sideList))

  if count == 1:
    print('Case #' + str(i+1) + ': equilateral')
  elif count == 2:
    print('Case #' + str(i+1) + ': isosceles')
  elif count == 3:
    print('Case #' + str(i+1) + ': scalene')

