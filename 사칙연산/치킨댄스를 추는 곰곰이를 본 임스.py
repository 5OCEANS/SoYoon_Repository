import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())

aMax = A // 2
bMax = B

print(min(N, aMax + bMax))