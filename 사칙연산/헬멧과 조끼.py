import sys

N, M = map(int, sys.stdin.readline().strip().split())

hList = list(map(int, sys.stdin.readline().strip().split()))
aList = list(map(int, sys.stdin.readline().strip().split()))

print(max(hList) + max(aList))