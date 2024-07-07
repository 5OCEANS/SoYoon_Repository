import sys

max = 0
maxScore = 0

for i in range(5):
  numList = list(map(int, sys.stdin.readline().strip().split()))

  if maxScore < sum(numList):
    maxScore = sum(numList)
    max = i + 1

print(max, maxScore)