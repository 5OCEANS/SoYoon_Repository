import sys

string = sys.stdin.readline().strip()

backwards = string[::-1]

if string == backwards:
  print('true')
else:
  print('false')