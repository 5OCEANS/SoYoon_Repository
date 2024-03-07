import sys

g, p, t = map(int, sys.stdin.readline().split())

kitNum = 0

kitNum += g

kitNum += p*t

if kitNum < g*p:
  print(2)
elif kitNum > g*p:
  print(1)
elif kitNum == g*p:
  print(0)