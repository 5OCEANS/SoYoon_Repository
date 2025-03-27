import sys

N, M = map(int, sys.stdin.readline().strip().split())
nList = list(map(int, sys.stdin.readline().strip().split()))
mList = list(map(int, sys.stdin.readline().strip().split()))
num = sum(nList)
for m in mList:
  if m == 0:
    continue
  num *= m
print(num)