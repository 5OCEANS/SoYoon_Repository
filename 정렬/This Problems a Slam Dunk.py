import sys

firstList = list(map(int, sys.stdin.readline().strip().split()))
secondList = list(map(int, sys.stdin.readline().strip().split()))

firstList.sort(reverse=True)
secondList.sort(reverse=True)
count = 0

for i in range(5):
  if firstList[i] > secondList[i]:
    count += 1
print(count)