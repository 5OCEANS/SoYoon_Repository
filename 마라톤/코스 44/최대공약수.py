import sys, math

A, B = map(int, sys.stdin.readline().strip().split())
print(math.gcd(A, B)*"1")