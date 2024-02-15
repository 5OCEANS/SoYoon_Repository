import sys

N = int(sys.stdin.readline())

def factorial(n):
  if n == 1 or n == 0:
    return 1
  res = n * factorial(n-1)
  return res

print(factorial(N))