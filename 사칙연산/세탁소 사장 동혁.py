import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  q, d, n, p = 0, 0, 0, 0
  C = int(sys.stdin.readline().strip())

  q = C // 25
  C = C % 25
  d = C // 10
  C = C % 10
  n = C // 5
  p = C % 5

  print(q, d, n , p)


# 25 10 5 1