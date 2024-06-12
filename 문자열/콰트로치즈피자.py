import sys

N = int(sys.stdin.readline().strip())

cheeseList = []

stringList = list(sys.stdin.readline().strip().split())

for i in range(N):
  if stringList[i][-6:] == 'Cheese':
    cheeseList.append(stringList[i])

cheeseSet = set(cheeseList)

if len(cheeseSet) >= 4:
  print('yummy')
else:
  print('sad')