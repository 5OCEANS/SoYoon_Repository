import sys

string = sys.stdin.readline().strip()

happyCnt = string.count(':-)')
sadCnt = string.count(':-(')

if happyCnt > sadCnt:
  print('happy')
elif happyCnt < sadCnt:
  print('sad')
elif happyCnt == 0 and sadCnt == 0:
  print('none')
else:
  print('unsure')