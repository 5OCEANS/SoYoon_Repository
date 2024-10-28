import sys

while True:
  try:
    sideList = list(map(int, sys.stdin.readline().strip().split()))
    sortedSideList = sorted(sideList, reverse=True)
    if sortedSideList.count(0) == 3:
      break
    if sortedSideList[0] >= (sortedSideList[1]+sortedSideList[2]):
      print('Invalid')
    elif len(set(sortedSideList)) == 1:
      print('Equilateral')
    elif len(set(sortedSideList)) == 2:
      print('Isosceles')
    elif len(set(sortedSideList)) == 3:
      print('Scalene')
  
  except:
    break