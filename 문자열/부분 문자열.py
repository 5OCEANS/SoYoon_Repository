import sys

S = sys.stdin.readline().strip()

P = sys.stdin.readline().strip()

if P in S:
  print(1)
else:
  print(0)