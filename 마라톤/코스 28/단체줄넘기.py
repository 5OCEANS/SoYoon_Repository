import sys

N = int(sys.stdin.readline())
heightList = list(map(int, sys.stdin.readline().strip().split()))

heightList.sort()

leftSet = set(heightList)
leftList = list(leftSet)
for i in range(len(leftList)):
  heightList.remove(leftList[i])
rightSet = set(heightList)
print(len(leftSet)+len(rightSet))