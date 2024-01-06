caseCnt = int(input())

for i in range(0, caseCnt):
  h, w, n = map(int, input().split())

  y = (n % h)
  xx = n // h + 1
  if y == 0:
    y = h
    xx -= 1
    
  print("%d%02d" % (y, xx))