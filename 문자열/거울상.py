import sys

while True:
  try:
    string = sys.stdin.readline().strip()
    string = string[::-1]
    newString = ''

    if string == '#':
      break

    for i in range(len(string)):
      if string[i] == 'b':
        newString += 'd'
      elif string[i] == 'd':
        newString += 'b'
      elif string[i] == 'p':
        newString += 'q'
      elif string[i] == 'q':
        newString += 'p'
      elif string[i] == 'i':
        newString += 'i'
      elif string[i] == 'o':
        newString += 'o'
      elif string[i] == 'v':
        newString += 'v'
      elif string[i] == 'w':
        newString += 'w'
      elif string[i] == 'x':
        newString += 'x'
      else:
        print('INVALID')
        break
    else:  
      print(newString)
  
  except:
    break