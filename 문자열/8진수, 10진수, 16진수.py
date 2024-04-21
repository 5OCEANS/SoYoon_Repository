import sys

X = sys.stdin.readline().strip()

if X.startswith('0x'):
  print(int(X, 16))
elif X.startswith('0'):
  print(int(X, 8))
else:
  print(int(X))