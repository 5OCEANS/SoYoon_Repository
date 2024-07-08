import sys

while True:
  num1, num2 = map(int, sys.stdin.readline().strip().split())

  if num1 == num2 and num1 == 0:
    break

  if num2 % num1 == 0:
    print('factor')
  elif num1 % num2 == 0:
    print('multiple')
  else:
    print('neither')