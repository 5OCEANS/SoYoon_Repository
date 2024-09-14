import sys

N = int(sys.stdin.readline())
danceset = set()
danceset.add('ChongChong')

for i in range(N):
  a, b = sys.stdin.readline().strip().split()

  if a in danceset or b in danceset:
    danceset.add(a)
    danceset.add(b)

print(len(danceset))