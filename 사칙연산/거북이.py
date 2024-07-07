import sys

numList = map(int, sys.stdin.readline().strip().split())

sorted_numList = sorted(numList, reverse=True)

print(sorted_numList[1] * sorted_numList[3])