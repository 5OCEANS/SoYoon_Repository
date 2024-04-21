import sys

N = int(sys.stdin.readline())

original = sys.stdin.readline().strip()

overwrite = ''

if N % 2 == 1:
  overwrite = original.replace('0', '3').replace('1', '0').replace('3', '1')
else:
  overwrite = original

test = sys.stdin.readline().strip()

if overwrite == test:
  print('Deletion succeeded')
else:
  print('Deletion failed')