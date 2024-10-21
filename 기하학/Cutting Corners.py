import sys, math

w, h = map(int, sys.stdin.readline().strip().split())

print((w+h)-math.sqrt(w**2+h**2))