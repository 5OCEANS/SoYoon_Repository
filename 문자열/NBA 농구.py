import sys

string = sys.stdin.readline().strip()
newString = ''

if '_' in string: # C++
  index = 0
  if string[index] == '_' or string[index].isupper():
    print('Error!')
    exit(0)
  elif string[-1] == '_':
    print('Error!')
    exit(0)

  while index < len(string):
    if string[index] == '_':
      index += 1
      if string[index].islower():
        newString += string[index].upper()
        index += 1
        continue
      else:
        print('Error!')
        exit(0)
    else:
      if string[index].islower():
        newString += string[index]
        index += 1
      else:
        print('Error!')
        exit(0)   
  print(newString)

else: # Java
  for i in range(len(string)):
    if i == 0 and string[i].isupper():
      print('Error!')
      exit(0)
    if string[i].islower():
      newString += string[i]
    elif string[i].isupper():
      newString += ('_' + string[i].lower())
    else:
      print('Error!')
      exit(0)
  else:
    print(newString)
