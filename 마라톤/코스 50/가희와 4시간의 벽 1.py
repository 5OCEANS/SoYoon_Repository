import sys

sab = int(sys.stdin.readline().strip())
fab = int(sys.stdin.readline().strip())

if sab > fab:
  print("flight")
else:
  print('high speed rail')