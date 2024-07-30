
# N = 1 1
# N = 2 10 1
# N = 3 100 101 2
# N = 4 1001 1010 1000 3
# N = 5 10101 10100 10010 10001 10000  5

import sys

N = int(sys.stdin.readline())

a = 1
b = 1

for i in range(N-1):
  a, b = b, a+b

print(a)