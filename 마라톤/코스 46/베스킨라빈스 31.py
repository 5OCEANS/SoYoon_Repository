import sys

A = int(sys.stdin.readline().strip())

for i in range(1, A+1):
  gap = i+1
  if 30 % gap == 0:
    print(i)