import sys

h, i, a, r, c = map(int, sys.stdin.readline().strip().split())
print((h*i)-(a*r*c))