import sys, re

S = sys.stdin.readline().strip()

S = re.sub('pi', ' ', S)
S = re.sub('ka', ' ', S)
S = re.sub('chu', ' ', S)

if S.strip() == '':
  print('YES')
else:
  print('NO')