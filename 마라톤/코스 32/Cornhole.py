import sys

H1, B1 = map(int, sys.stdin.readline().strip().split())
H2, B2 = map(int, sys.stdin.readline().strip().split())

P1 = (H1 * 3) + B1
P2 = (H2 * 3) + B2

if P1 == P2:
  print("NO SCORE")
elif P2 < P1:
  print("1 %d" %(P1-P2))
else:
  print("2 %d" %(P2 - P1))