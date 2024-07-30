import sys

# n = 1 1
# n = 2 2
# n = 3 001 100 111 3
# n = 4 0011 0000 1001 1100 1111 5
# n = 5 10011 10000 11001 11100 1111 00001 00100 00111 8

a = 1
b = 2

N = int(sys.stdin.readline())

for i in range(N-1):
  a, b = b, (a+b)%15746

print(a)