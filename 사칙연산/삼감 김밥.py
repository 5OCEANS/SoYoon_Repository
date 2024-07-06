import sys

X, Y = map(int, sys.stdin.readline().strip().split())

minPrice = X * (1000/Y)

N = int(sys.stdin.readline().strip())

for i in range(N):
  iX, iY = map(int, sys.stdin.readline().strip().split())

  price = iX * (1000/iY)

  if minPrice > price:
    minPrice = price
  
print(minPrice)