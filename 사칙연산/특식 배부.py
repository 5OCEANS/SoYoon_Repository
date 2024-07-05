import sys

N = int(sys.stdin.readline())

chickenList = list(map(int, sys.stdin.readline().strip().split()))

res = 0

for i in range(3):
  if chickenList[i] < N:
    res += chickenList[i]
  else:
    res += N

print(res)