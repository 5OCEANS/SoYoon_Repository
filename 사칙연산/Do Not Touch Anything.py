import sys

R, C, N = map(int, sys.stdin.readline().strip().split())

RN= R//N
if R%N != 0:
  RN += 1

CN = C//N
if C%N != 0:
  CN += 1

print(RN*CN)