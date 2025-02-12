import sys, math

N = int(sys.stdin.readline())
numList = list()
for i in range(N):
  x, y = map(int, sys.stdin.readline().strip().split())
  numList.append((x, y))

maxDistance = 0
smallIndex = 0
largeIndex = 0

for i in range(N-1):
  for j in range(i+1, N):
    distance = math.sqrt((numList[i][0]-numList[j][0])**2 + (numList[i][1]-numList[j][1])**2)
    if distance > maxDistance:
      maxDistance = distance
      smallIndex = i+1
      largeIndex = j+1
print(smallIndex, largeIndex)