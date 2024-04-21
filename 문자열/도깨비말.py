import sys

while True:
  try:

    string = sys.stdin.readline().strip()

    if string == '#':
      break

    for i in range(len(string)):
      if string[i] in ['a', 'e', 'i', 'o', 'u']:
        string = string[i:] + string[:i] + 'ay'
        break
    else:
      string = string + 'ay'

    print(string)

  except:
    break