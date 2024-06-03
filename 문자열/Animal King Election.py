import sys

tigerCnt = 0

lionCnt = 0

for i in range(9):
  if sys.stdin.readline().strip() == 'Lion':
    lionCnt += 1
  else:
    tigerCnt += 1

print('Lion' if lionCnt > tigerCnt else 'Tiger')