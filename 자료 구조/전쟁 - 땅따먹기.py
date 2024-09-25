# 시간 초과 
import sys

n = int(sys.stdin.readline())

for i in range(n):
  tList = list(map(int, sys.stdin.readline().strip().split()))
  tSet = set(tList[1:])

  for j in tSet:
    if tList.count(j) > (tList[0] / 2):
      print(j)
      break
  else:
    print('SYJKGW')

import sys
from collections import Counter

n = int(sys.stdin.readline())

for i in range(n):
  tList = list(map(int, sys.stdin.readline().strip().split()))
  tSet = set(tList[1:])
  tCounter = Counter(tList[1:])

  for j in tSet:
    if tCounter[j] > (tList[0] / 2):
      print(j)
      break
  else:
    print('SYJKGW')