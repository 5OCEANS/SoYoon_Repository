import sys

N, C, T, P = map(int, sys.stdin.readline().strip().split())
print((N-1)//C * T * P)