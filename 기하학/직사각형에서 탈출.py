import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

print(min(x, h-y, w-x, y))