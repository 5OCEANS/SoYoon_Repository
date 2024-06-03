import sys

n = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

twoCnt = string.count('2')
eCnt = string.count('e')

if twoCnt > eCnt:
  print('2')
elif twoCnt == eCnt:
  print('yee')
else:
  print('e')