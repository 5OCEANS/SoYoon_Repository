import sys

A, B = map(int, sys.stdin.readline().strip().split())

M = (B-A)/400

winPersent = 1/(1+pow(10, M))

print(winPersent)