import sys

t = int(sys.stdin.readline())

for i in range(t):
  N = int(sys.stdin.readline())
  print(N*(N+1)//2, N**2, N**2+N)