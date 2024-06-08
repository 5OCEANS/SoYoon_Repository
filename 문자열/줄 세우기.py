import sys

N = int(sys.stdin.readline())
nameList = []

for i in range(N):
  name = sys.stdin.readline().strip()
  nameList.append(name)

increasingList = sorted(nameList)
decreasingList = sorted(nameList,reverse=True)

if increasingList == nameList:
  print('INCREASING')
elif decreasingList == nameList:
  print('DECREASING')
else:
  print('NEITHER')