import sys

burger = 3000
drink = 3000

for i in range(3):
  price = int(sys.stdin.readline())
  if burger > price:
    burger = price

for i in range(2):
  price = int(sys.stdin.readline())
  if drink > price:
    drink = price

print(burger + drink - 50)