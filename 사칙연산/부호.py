import sys

for i in range(3):
  N = int(sys.stdin.readline())
  S = 0
  for j in range(N):
    num = int(sys.stdin.readline())
    S += num
  if S == 0:
    print(0)
  elif S > 0:
    print('+')
  else:
    print('-')