import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())

time = 0

if A < 0:
  time = abs(A) * C + D + B * E
elif A > 0:
  time = (B - A) * E

print(time)