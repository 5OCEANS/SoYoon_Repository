import sys, math

t = 1
while True:
  try:
    w, d = map(int, sys.stdin.readline().strip().split())
    if w == 0 and d == 0:
      break
    n = math.log((810/(d/w)), 2)
    x = n * 5730
    if x < 10000:
      x = (round(x/100)) * 100
    elif x >= 10000:
      x = (round(x/1000)) * 1000

    print("Sample #%d" %(t))
    print("The approximate age is %d years." %(x))
    print()
    t += 1
  
  except:
    break