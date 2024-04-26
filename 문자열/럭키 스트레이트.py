import sys

N = sys.stdin.readline().strip()

firstN = list(map(int, list(N[:len(N)//2])))
secondN = list(map(int,list(N[len(firstN):])))

if sum(firstN) == sum(secondN):
  print('LUCKY')
else:
  print('READY')