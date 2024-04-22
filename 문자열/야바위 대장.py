import sys

S = list(sys.stdin.readline().strip())

T = int(sys.stdin.readline())

for i in range(T):
  A, B = map(int, sys.stdin.readline().strip().split())

  tmp = S[A]
  S[A] = S[B]
  S[B] = tmp

for i in S:
  print(i, end = '')