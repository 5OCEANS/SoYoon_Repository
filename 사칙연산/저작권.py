import sys

A, I = map(int, sys.stdin.readline().strip().split())

print(A*(I-1)+1)