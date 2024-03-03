import sys

N, W, H, L = map(int, sys.stdin.readline().strip().split())

maxCow = 0

maxCow = (W // L) * (H // L)
  
if maxCow >= N:
  maxCow = N

print(maxCow)