import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  N, M = map(int, sys.stdin.readline().strip().split())

  U = 2 * M - N

  print(U, M - U)