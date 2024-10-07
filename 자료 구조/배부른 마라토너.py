import sys

N = int(sys.stdin.readline())
namelist = set()

for i in range(2*N-1):
  name = sys.stdin.readline().strip()
  if name in namelist:
    namelist.remove(name)
  else:
    namelist.add(name)

for value in namelist:
  print(value)