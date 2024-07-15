import sys

N = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))

print(B[0], end = ' ')

sumA = B[0]

for i in range(1, len(B)):
  sumNum = B[i] * (i + 1)
  print(sumNum - sumA, end = ' ')
  sumA = sumNum
