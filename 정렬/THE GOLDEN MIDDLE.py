import sys

numList = list(map(int, sys.stdin.readline().strip().split()))
numList.sort()
print(numList[1])