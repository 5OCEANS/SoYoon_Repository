import sys

while True:
  try:

    x, y = map(float, sys.stdin.readline().strip().split())
    if x == 0 and y == 0:
      print('AXIS')
      break 
    
    if x == 0 or y == 0:
      print('AXIS')
    elif x < 0:
      if y < 0:
        print('Q3')
      else:
        print('Q2')
    else:
      if y < 0:
        print('Q4')
      else:
        print('Q1')
  except:
    break