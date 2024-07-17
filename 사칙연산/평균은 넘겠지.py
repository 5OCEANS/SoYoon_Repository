import sys

C = int(sys.stdin.readline().strip())

for i in range(C):
  Nstring = list(map(int, sys.stdin.readline().strip().split()))
  N = Nstring[0]
  Nlist = Nstring[1:]

  ans = 0

  Navg = sum(Nlist) / N

  for j in range(N):
    if Nlist[j] > Navg:
      ans += 1
  
  print('%0.3f%%' %((ans / N)* 100))
