import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

price = 0

for i in range(N):
  a, b = map(int, sys.stdin.readline().split())
  price += (a*b)

if X == price:
  print('Yes')
else:
  print('No')