import sys

a = 0
b = 1

n = int(sys.stdin.readline().strip())

for i in range(n):
  a, b = b, a + b

print(a)