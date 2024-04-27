import sys

N = int(sys.stdin.readline())

s = sys.stdin.readline().strip()

if s[N-1] in 'qwertasdfgzxcv':
  print(1)
else:
  print(0)