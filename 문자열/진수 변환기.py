import sys

m, n = map(int, sys.stdin.readline().split())
mns = ''

if m == 0:
  mns = '0'

while m > 0:
  mns += str(hex(m%n)[2:]).upper()

  m //= n

mns = mns[::-1]
print(mns)