import sys

string = sys.stdin.readline().strip()

prev = string[0]

for i in range(1, len(string)):
  if string[i] == 's' and string[i] == prev:
    print('hiss')
    break
  else:
    prev = string[i]
else:
  print('no hiss')