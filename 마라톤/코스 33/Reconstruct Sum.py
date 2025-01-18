import sys

n = int(sys.stdin.readline())
numList = list()
for i in range(n):
  num = int(sys.stdin.readline().strip())
  numList.append(num)

for i in range(n):
  sumNum = numList[i]
  actualSumNum = sum(numList[0:i]) + sum(numList[i+1:n])
  if sumNum == actualSumNum:
    print(sumNum)
    break
else:
  print('BAD')