import sys

N = int(sys.stdin.readline())
for i in range(N):
  alist = list(map(int, sys.stdin.readline().strip().split()))[1:]
  blist = list(map(int, sys.stdin.readline().strip().split()))[1:]
  isStarCountSame = (alist.count(4) == blist.count(4))
  isCircleCountSame = (alist.count(3) == blist.count(3))
  isSquareCountSame = (alist.count(2) == blist.count(2))
  isTriangleCountSame = (alist.count(1) == blist.count(1))

  if not isStarCountSame:
    print('A') if alist.count(4) > blist.count(4) else print('B')
  elif not isCircleCountSame:
    print('A') if alist.count(3) > blist.count(3) else print('B')
  elif not isSquareCountSame:
    print('A') if alist.count(2) > blist.count(2) else print('B')
  elif not isTriangleCountSame:
    print('A') if alist.count(1) > blist.count(1) else print('B')
  else:
    print('D')