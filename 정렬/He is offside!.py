import sys

while True:
  try:
    A, D = map(int, sys.stdin.readline().strip().split())
    if A == 0 and D == 0:
      break
    aList = list(map(int, sys.stdin.readline().strip().split()))
    dList = list(map(int, sys.stdin.readline().strip().split()))
    aList.sort()
    dList.sort()
    for i in range(len(aList)):
      if dList[0] == dList[1] == aList[i]:
        print('N')
        break
      elif dList[1] == aList[i]:
        print('N')
        break
      if dList[1] > aList[i]:
        print('Y')
        break
    else:
      print('N')
  except:
    break
