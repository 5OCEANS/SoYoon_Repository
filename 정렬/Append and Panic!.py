import sys

s = sys.stdin.readline().strip()

n = len(s)

for i in range(1, n):
  t = s[:i]
  sorted_unique = ''.join(sorted(set(t)))
  if t + sorted_unique == s:
    print(i)
    break