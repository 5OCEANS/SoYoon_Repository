import sys

N = int(sys.stdin.readline().strip())
maxReward = 0

for i in range(N):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  numDic = {}

  for j in range(1, 7):
    numDic[j] = numList.count(j)
    if numDic[j] == 3:
      reward = 10000 + j*1000
      break
    elif numDic[j] == 2:
      reward = 1000 + j*100
      break
  else:
    reward = max(numList) * 100
  
  if maxReward < reward:
    maxReward = reward

print(maxReward)