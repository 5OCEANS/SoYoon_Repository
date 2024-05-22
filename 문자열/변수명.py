import sys

num, string = sys.stdin.readline().strip().split()
splitpoint = []

camel = ''
snake = ''
pascal = ''

if num == '1':
  print(string)
  for i in range(len(string)):
    if string[i].isupper():
      snake += ('_' + string[i].lower())
    else:
      snake += string[i]
  print(snake)
  print(string[0].upper() + string[1:])

elif num == '2':
  i = 0
  while i < len(string):
    if string[i] == '_':
      camel += string[i+1].upper()
      i += 1
    else:
      camel += string[i]
    i += 1
  print(camel)
  print(string)
  print(camel[0].upper() + camel[1:])
elif num == '3':
  camel = string[0].lower() + string[1:]
  print(camel)
  for i in range(len(camel)):
    if camel[i].isupper():
      snake += ('_' + camel[i].lower())
    else:
      snake += camel[i]
  print(snake)
  print(string)