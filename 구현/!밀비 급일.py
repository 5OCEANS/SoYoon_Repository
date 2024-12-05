import sys

while True:
  string = sys.stdin.readline().strip()
  if string == 'END':
    break
  print(string[::-1])