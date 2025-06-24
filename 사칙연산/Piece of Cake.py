import sys

n, h, v = map(int, sys.stdin.readline().strip().split())

res = max(h*v, (n-h)*v, h*(n-v), (n-h)*(n-v))
print(res * 4)