import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())

X = P * A
Y = 0

if C < P:
  Y = B + D * (P - C)
else:
  Y = B

if X < Y:
  print(X)
else:
  print(Y)