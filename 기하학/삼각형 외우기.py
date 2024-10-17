import sys

angleList = []

for i in range(3):
  angle = int(sys.stdin.readline())
  angleList.append(angle)

if sum(angleList) != 180:
  print('Error')
else:
  count = len(set(angleList)) 

  if count == 3:
    print('Scalene')
  elif count == 2:
    print('Isosceles')
  else:
    print('Equilateral')