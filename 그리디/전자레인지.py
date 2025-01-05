import sys

a = 5*60
b = 60
c = 10
aans = 0
bans = 0
cans = 0

T = int(sys.stdin.readline().strip())
if a <= T:
  aans += T//a
  T = T % a
if b <= T:
  bans += T//b
  T = T % b
if c <= T:
  cans += T//c
  T = T % c
if T != 0:
  print(-1)
else:
  print(aans, bans, cans)