import sys

apple, pear = map(int, sys.stdin.readline().strip().split())

axel = apple * 7
petra = pear * 13

if axel > petra:
  print('Axel')
elif axel < petra:
  print('Petra')
else:
  print('lika')