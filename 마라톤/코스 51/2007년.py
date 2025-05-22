import sys

x, y = map(int, sys.stdin.readline().strip().split())
count = 0
if x >= 2:
  count += 31
if x >= 3:
  count += 28
if x >= 4:
  count += 31
if x >= 5:
  count += 30
if x >= 6:
  count += 31
if x >= 7:
  count += 30
if x >= 8:
  count += 31
if x >= 9:
  count += 31
if x >= 10:
  count += 30
if x >= 11:
  count += 31
if x >= 12:
  count += 30
count += y

result = count % 7
if result == 0:
  print('SUN')
elif result == 1:
  print('MON')
elif result == 2:
  print('TUE')
elif result == 3:
  print('WED')
elif result == 4:
  print('THU')
elif result == 5:
  print('FRI')
elif result == 6:
  print('SAT')


import sys

D = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, sys.stdin.readline().strip().split())
M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = sum(M[:x]) + y
print(D[(T % 7)])