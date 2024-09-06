import sys

C, K, P = map(int, sys.stdin.readline().strip().split())

result = 0

for i in range(C+1):
  result += i * (K + P*i)

print(result)