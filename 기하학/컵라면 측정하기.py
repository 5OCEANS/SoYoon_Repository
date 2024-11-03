import sys

K = int(sys.stdin.readline())

d1, d2 = map(int, sys.stdin.readline().strip().split())

print(K**2 - ((d1-d2)/2)**2)