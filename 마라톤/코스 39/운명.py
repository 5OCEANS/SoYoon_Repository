import sys
from collections import Counter

X, K = map(int, sys.stdin.readline().strip().split())
socksList = list(map(int, sys.stdin.readline().strip().split()))
leftSocksList = socksList[0:X]
rightSocksList = socksList[X:]
rightSocksCount = Counter(rightSocksList)
count = 0
for leftsocks in leftSocksList:
  count += (X- rightSocksCount[leftsocks])

print(count)