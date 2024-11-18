import sys

s1, s2 = map(int, sys.stdin.readline().strip().split())

print('E') if (s2 / 2 <= s1) else print('H')