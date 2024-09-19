import sys

string = list(sys.stdin.readline().strip().split())
stringset = set(string)

if len(string) == len(stringset):
  print('yes')
else:
  print('no')