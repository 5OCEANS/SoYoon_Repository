import sys

nList = list(map(int, sys.stdin.readline().split()))
nList.sort()

print(nList[1])