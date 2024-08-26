import sys

s = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = int(sys.stdin.readline())

sum = 1 * s + 2 * m + 3 * l

if sum >= 10:
  print('happy')
else:
  print('sad')

import sys

sum = 0

for i in range(3):
  num = int(sys.stdin.readline())
  sum += (i+1) * num

if sum >= 10:
  print('happy')
else:
  print('sad')
