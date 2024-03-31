import sys

mbti = sys.stdin.readline().strip()


if mbti[0] == 'I':
  print('E', end = '')
else:
  print('I', end='')

if mbti[1] == 'S':
  print('N', end = '')
else:
  print('S', end ='')

if mbti[2] == 'T':
  print('F', end ='')
else:
  print('T', end = '')

if mbti[3] == 'J':
  print('P')
else:
  print('J')
