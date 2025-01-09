import sys

def calculate_minimum_moves(a, b, x, y):
  if a == 0:
    if x == 0 and y < b:  
      return 3
    return 1
  if b == 0:
    if y == 0 and x < a:  
      return 3
    return 1

  return 2

a, b = map(int, sys.stdin.readline().strip().split())
x, y = map(int, sys.stdin.readline().strip().split())

print(calculate_minimum_moves(a, b, x, y))