import sys

while True:
  M, F = map(int, sys.stdin.readline().strip().split())

  if M == 0 and F == 0:
    break

  print(M+F)