numCnt = int(input())
numList = list(map(int, input().split()))

max = -1000000
min = 1000000

for i in range(0, numCnt):
  if max < numList[i]:
    max = numList[i]
  if min > numList[i]:
    min = numList[i]
    
print(min, max)