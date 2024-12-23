import sys

N = int(sys.stdin.readline())
criminal = ''
for _ in range(N):
  name = sys.stdin.readline().strip()
  if 'S' in name:
    criminal = name
print(criminal)