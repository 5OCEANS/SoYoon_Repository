import sys

n, m = map(int, sys.stdin.readline().strip().split())
aSet = set(map(int, sys.stdin.readline().strip().split()))
bSet = set(map(int, sys.stdin.readline().strip().split()))

print(len(aSet - bSet) + len(bSet - aSet))