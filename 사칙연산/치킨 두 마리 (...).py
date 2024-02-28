import sys

A, B = map(int, sys.stdin.readline().strip().split())
C = int(sys.stdin.readline().strip())

hap = A+B

if hap < 2*C:
  print(hap)
elif hap >= 2*C:
  print(hap-2*C)