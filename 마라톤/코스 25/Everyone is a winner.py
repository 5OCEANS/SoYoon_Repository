import sys

M, K = map(int, sys.stdin.readline().strip().split())
print('Yes') if M % K == 0 else print('No')