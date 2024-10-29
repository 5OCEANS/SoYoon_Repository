import sys, math

count = 0
while True:
  try:
    count += 1

    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == b == c == 0:
      break

    if a == -1:
      if (c**2 - b**2) > 0:
        a = math.sqrt(c**2 - b**2)
        print('Triangle # ' + str(count))
        print('a = ' + '%0.3f' %(a))
      else:
        print('Triangle # ' + str(count))
        print('Impossible.')
        print()
    elif b == -1:
      if (c**2 - a**2) > 0:
        b = math.sqrt(c**2 - a**2)
        print('Triangle # ' + str(count))
        print('b = ' + '%0.3f' %(b))
      else:
        print('Triangle # ' + str(count))
        print('Impossible.')
        print()
    elif c == -1:
      if (a**2 + b**2) > 0:
        c = math.sqrt(a**2 + b**2)
        print('Triangle # ' + str(count))
        print('c = ' + '%0.3f' %(c))
      else:
        print('Triangle # ' + str(count))
        print('Impossible.')
        print()
    print()

  except:
    break