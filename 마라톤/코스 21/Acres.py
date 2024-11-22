import sys, math

w, h = map(int, sys.stdin.readline().strip().split())
print(math.ceil((w*h)/(4840*5)))