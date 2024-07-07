import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  evenList = []

  for j in range(len(numList)):
    if numList[j] % 2 == 0:
      evenList.append(numList[j])
  
  sorted_evenList = sorted(evenList)

  print(sum(evenList), sorted_evenList[0])