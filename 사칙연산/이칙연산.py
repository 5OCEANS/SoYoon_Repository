import sys

A, B, C = map(int, sys.stdin.readline().split())

multiplicationFirst = int(A * B / C)
divisionFirst = int(A / B * C)

print(max(multiplicationFirst, divisionFirst))