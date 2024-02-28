import sys

S, T, D = map(int, sys.stdin.readline().strip().split())

time = D/(2*S)
print(int(time*T))