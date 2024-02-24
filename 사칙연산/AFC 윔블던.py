import sys

hap, cha = map(int, sys.stdin.readline().split())

if hap + cha < 0 or hap-cha < 0 or (hap+cha) % 2 :
  print(-1)
else:
  a = (hap + cha) // 2
  b = hap - a
  print(max(a, b), min(a, b))