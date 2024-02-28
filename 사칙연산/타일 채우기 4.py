import sys

N, M = map(int, sys.stdin.readline().strip().split())

nMax = N//2 * M
if N%2 != 0:
  nMax += M//2

mMax = M//2 * N
if M%2 != 0:
  mMax += N//2

print(max(nMax, mMax))