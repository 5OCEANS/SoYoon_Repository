import sys

startsWithL = False
startsWithK = False
startsWithP = False

for _ in range(3):
  string = sys.stdin.readline().strip()
  if string.startswith('l'):
    startsWithL = True
  elif string.startswith('k'):
    startsWithK = True
  elif string.startswith('p'):
    startsWithP = True

if startsWithL and startsWithK and startsWithP:
  print('GLOBAL')
else:
  print('PONIX')