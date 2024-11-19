import sys

while True:
  try:
    A, B = map(int, sys.stdin.readline().strip().split())
    if A == 0 and B == 0:
      break
    print(B - (B-A)*2)
  except:
    break