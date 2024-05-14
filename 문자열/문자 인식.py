import sys

N = int(sys.stdin.readline())
for i in range(N):
  stringList = []

  while True:
    try:
      string = sys.stdin.readline().strip()
      if string == '':
        break
      stringList += list(string)
    except:
      break

  ratio = round((len(stringList) - stringList.count('#')) / len(stringList) * 100, 1)
  
  if str(ratio).split('.')[1] == '0':
    ratio = int(ratio)

  print('Efficiency ratio is {0}%.'.format(ratio))