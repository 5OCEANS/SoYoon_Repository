import sys

A, B = map(int, sys.stdin.readline().split())

breadMax = A // 2
meatMax = B

print(min(breadMax, meatMax))