import sys

i = 1

while True:
  try:

    string = sys.stdin.readline().strip()
    string2 = sys.stdin.readline().strip()
    isSame = ''

    if string == 'END' and string2 == 'END':
      break

    if len(string) != len(string2):
      isSame = 'different'
    else:
      string = list(string)
      string2 = list(string2)
      for j in string:
        if j in string2:
          string2.remove(j)
        else:
          isSame = 'different'
          break
      else:
        isSame = 'same'

    print('Case %d:' %i, isSame)
    i += 1

  except:
    break


import collections
import sys

idx=1
while True:
    a=sys.stdin.readline().rstrip()
    b=sys.stdin.readline().rstrip()

    if a=='END' and b=='END':
        break

    if collections.Counter(a)==collections.Counter(b):
        print(f'Case {idx}: same')
    else:
        print(f'Case {idx}: different')

    idx+=1