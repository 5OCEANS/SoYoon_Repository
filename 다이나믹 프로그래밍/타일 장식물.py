import sys

N = int(sys.stdin.readline())

a = 1
b = 1

for i in range(N-1):
  a, b = b, a+b

print(a*2 + b*2)