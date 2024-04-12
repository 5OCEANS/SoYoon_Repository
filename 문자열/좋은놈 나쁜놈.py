import sys

n = int(sys.stdin.readline())

for i in range(n):
  hero = sys.stdin.readline().strip()

  gcnt = 0
  bcnt = 0

  judgment = ''

  for j in range(len(hero)):
    if hero[j].lower() == 'g':
      gcnt += 1
    elif hero[j].lower() == 'b':
      bcnt += 1
    
  if gcnt > bcnt:
    judgment = 'GOOD'
  elif gcnt == bcnt:
    judgment = 'NEUTRAL'
  else:
    judgment = 'A BADDY'
  
  print('%s is %s' %(hero, judgment))