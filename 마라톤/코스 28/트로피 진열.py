import sys

N = int(sys.stdin.readline())
leftHeight = 0
leftCount = 0
rightHeight = 0
rightCount = 0
trophy = list()

for i in range(N):
  height = int(sys.stdin.readline())
  trophy.append(height)

for i in range(N):
  if leftHeight < trophy[i]:
    leftCount += 1
    leftHeight = trophy[i]
    continue
  else:
    continue
print(leftCount)

trophy = trophy[::-1]

for i in range(N):
  if rightHeight < trophy[i]:
    rightCount += 1
    rightHeight = trophy[i]
    continue
  else:
    continue
print(rightCount)