import sys

L = int(sys.stdin.readline().strip())
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())

koreanDay = A//C

if A%C != 0:
  koreanDay += 1

mathDay = B//D

if B%D !=0:
  mathDay += 1

print(L-max(koreanDay, mathDay))