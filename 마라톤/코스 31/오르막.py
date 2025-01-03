import sys

numList = list(map(int, sys.stdin.readline().strip().split()))
sortedNumList = sorted(numList)

for i in range(len(numList)):
  if numList[i] != sortedNumList[i]:
    print("Bad")
    break
else:
  print("Good")