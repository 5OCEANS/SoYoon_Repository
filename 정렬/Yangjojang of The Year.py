import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())
  max = -1
  school = ""

  for j in range(N):
    S, L =  sys.stdin.readline().strip().split()

    if int(L) > max:
      school = S
      max = int(L)

  print(school)