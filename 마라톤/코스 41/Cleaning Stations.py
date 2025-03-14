import sys

K = int(sys.stdin.readline())
for num in range(K):
  n, m = map(int, sys.stdin.readline().strip().split())
  mList = list(map(int, sys.stdin.readline().strip().split()))
  fishList = list()
  maxScore = float('-inf')
  for i in range(n):
    numList = list(map(int, sys.stdin.readline().strip().split()))
    score = 0
    for j in range(m):
      score += (mList[j] * numList[j])
    if score > maxScore:
      maxScore = score
      fishList.clear()
      fishList.append(i+1)
    elif score == maxScore:
      fishList.append(i+1)
  fishList.sort()

  print('Data Set '+str(num+1)+':')
  for num in fishList:
    print(num)
  print()