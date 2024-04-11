import sys

string = list(sys.stdin.readline().strip().split())

abbreviation = ''

for i in range(len(string)):
  if i == 0:
    char = string[i][0].upper()
    abbreviation += char
  else:
    if string[i] == 'i':
      continue
    elif string[i] == 'pa':
      continue
    elif string[i] == 'te':
      continue
    elif string[i] == 'ni':
      continue
    elif string[i] == 'niti':
      continue
    elif string[i] == 'a':
      continue
    elif string[i] == 'ali':
      continue
    elif string[i] == 'nego':
      continue
    elif string[i] == 'no':
      continue
    elif string[i] == 'ili':
      continue
    else:
      char = string[i][0].upper()
      abbreviation += char

print(abbreviation)