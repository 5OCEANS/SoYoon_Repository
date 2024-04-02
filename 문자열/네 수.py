import sys

A, B, C, D = sys.stdin.readline().strip().split()

AB = A+B
CD = C+D

print(int(AB) + int(CD))