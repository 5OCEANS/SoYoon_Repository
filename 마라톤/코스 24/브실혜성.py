import sys

y, m, d = map(int, sys.stdin.readline().strip().split('-'))
N = int(sys.stdin.readline())

d += N
m += (d-1) // 30
d = (d-1) % 30 + 1
y += (m-1) // 12
m = (m-1) % 12 + 1

print('%d-%02d-%02d'%(y, m, d))