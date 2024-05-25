import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline(), 2)

twoPowK = pow(2, int(sys.stdin.readline()))

if M % twoPowK == 0:
  print('YES')
else:
  print('NO')