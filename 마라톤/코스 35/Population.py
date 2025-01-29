import sys

n = int(sys.stdin.readline())
for _ in range(n):
  p, t = map(int, sys.stdin.readline().strip().split())
  plus = t // 4
  minus = t // 7
  print(p + (plus - minus))