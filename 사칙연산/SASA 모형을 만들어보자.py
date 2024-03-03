import sys

S, M = map(int, sys.stdin.readline().split())

max = 0

if S >= M:
  max = M // 2
else: 
  max = S //2

print(max)