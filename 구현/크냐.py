import sys

while True:
  try:
    num1, num2 = map(int, sys.stdin.readline().strip().split())
    if num1 == 0 and num2 == 0:
      break
    print('Yes') if num1 > num2 else print('No')
  
  except:
    break