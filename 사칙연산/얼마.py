import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  s = int(sys.stdin.readline().strip())

  n = int(sys.stdin.readline().strip())
  for j in range(n):
    q, p = map(int, sys.stdin.readline().strip().split())

    s += q * p
  
  print(s)