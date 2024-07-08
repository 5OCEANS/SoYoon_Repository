import sys

totalPrice = int(sys.stdin.readline().strip())

for i in range(9):
  price = int(sys.stdin.readline().strip())

  totalPrice -= price

print(totalPrice)