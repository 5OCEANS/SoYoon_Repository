import sys
import math

M = int(sys.stdin.readline().strip())
colorList = list(map(int, sys.stdin.readline().strip().split()))
K = int(sys.stdin.readline().strip())
N = sum(colorList)
total = math.comb(N, K)
sameColor = 0
for s in colorList:
  sameColor += math.comb(s, K)
print(sameColor/total)