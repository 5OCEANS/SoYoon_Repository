# -1 1
# -2 -1
# -3 2
# -4 -3
# -5 5
# -6 -8
# 음수일 때 F(n-2) = F(n) - F(n-1)
# F(n) = (F(n-1) + F(n-2))

import sys

n = int(sys.stdin.readline())

if n > 0:
  a = 0
  b = 1

  for i in range(n):
    a, b = b, ((a+b)%1000000000)
  
  print(1)
  print(a)
elif n == 0:
  print(0)
  print(0)
elif n < 0:
  a = 0
  b = 1

  for i in range(abs(n)):
    a, b = b, a-b
  
  if a < 0:
    print(-1)
  elif a == 0:
    print(0)
  else:
    print(1)
  print(abs(a)%1000000000)
