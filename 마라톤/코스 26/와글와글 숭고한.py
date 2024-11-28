import sys

scoolList = list(map(int, sys.stdin.readline().strip().split()))
if sum(scoolList) >= 100:
  print('OK')
elif min(scoolList) == scoolList[0]:
  print('Soongsil')
elif min(scoolList) == scoolList[1]:
  print('Korea')
else:
  print('Hanyang')