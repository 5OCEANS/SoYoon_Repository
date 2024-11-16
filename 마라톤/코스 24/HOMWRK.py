import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())
  for j in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a+b, a*b)