import sys

K = int(sys.stdin.readline())

for i in range(K):
  h = int(sys.stdin.readline())
  actions = sys.stdin.readline().strip()

  print('Data Set %d:' %(i+1))

  for j in actions:
    if h == 0:
      break

    if j == 'c':
      h += 1
    elif j == 'b':
      h -= 1
  
  print(h)
  print()