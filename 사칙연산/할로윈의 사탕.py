import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  c, v = map(int, sys.stdin.readline().strip().split())

  print('You get %d piece(s) and your dad gets %d piece(s).' %(c//v, c%v))