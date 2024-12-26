import sys

N = int(sys.stdin.readline().strip())
if N == 0:
  print('divide by zero')
else:
  numList = list(map(int, sys.stdin.readline().strip().split()))
  avg = sum(numList) / len(numList)
  expectaionValue = 0
  numSet = set(numList)
  for i in numSet:
    expectaionValue += (i*(numList.count(i)/len(numList)))
  print('%0.2f' %(avg/expectaionValue))