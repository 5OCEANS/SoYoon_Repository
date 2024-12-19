import sys

T = int(sys.stdin.readline())
for _ in range(T):
  L, R, S = map(int, sys.stdin.readline().strip().split())
  L_S_distance = abs(abs(L)-abs(S))
  R_S_distance = abs(abs(R)-abs(S))
  res = 0
  if L_S_distance < R_S_distance:
    res = (2 * L_S_distance) + 1
  else:
    res = 2*(R_S_distance)
  print(res)


import sys

T = int(sys.stdin.readline())
for _ in range(T):
  L, R, S = map(int, sys.stdin.readline().strip().split())
  L_S_distance = S-L
  R_S_distance = R-S
  res = 0
  if L_S_distance < R_S_distance:
    res = (2 * L_S_distance) + 1
  else:
    res = 2*(R_S_distance)
  print(res)