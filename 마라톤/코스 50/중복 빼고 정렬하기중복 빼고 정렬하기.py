import sys

n = int(sys.stdin.readline().strip())
nList = list(set(map(int, sys.stdin.readline().strip().split())))
nList.sort()
print(*nList)