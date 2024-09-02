import sys

numList = map(int, sys.stdin.readline().strip().split())
print(sum(numList) * 5)