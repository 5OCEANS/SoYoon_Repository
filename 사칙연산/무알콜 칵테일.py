import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

I, J, K = map(int, sys.stdin.readline().strip().split())

min_value = min(A/I, B/J, C/K)

print(A-(min_value*I), B-(min_value*J), C-(min_value*K))