import sys

count = 1
while True:
  try:
    rwlList = list(map(int, sys.stdin.readline().strip().split()))

    if rwlList[0] == 0:
      break

    if rwlList[0]**2 >= ((rwlList[1]/2)**2 + (rwlList[2]/2)**2):
      print('Pizza ' + str(count) + ' fits on the table.')
    else:
      print('Pizza ' + str(count) + ' does not fit on the table.')

    count += 1
  except:
    break