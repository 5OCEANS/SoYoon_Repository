import sys, math

e, f, c = map(int ,sys.stdin.readline().strip().split())

totalAns = (e+f) // c

empty = ((e + f) % c) + totalAns

while empty // c >= 1:
  totalAns += (empty // c)
  empty = (empty % c) + (empty // c)

print(totalAns)