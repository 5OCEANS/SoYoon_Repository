import sys

while True:
  try:
    word = sys.stdin.readline().strip()

    if word == '#':
      break

    word = word[::-1]
    numSum = 0

    for i in range(len(word)):
      num = 100

      if word[i] == '-':
        num = 0
      elif word[i] == '\\':
        num = 1
      elif word[i] == '(':
        num = 2
      elif word[i] == '@':
        num = 3
      elif word[i] == '?':
        num = 4
      elif word[i] == '>':
        num = 5
      elif word[i] == '&':
        num = 6
      elif word[i] == '%':
        num = 7
      elif word[i] == '/':
        num = -1

      numSum += num * pow(8, i)

    print(numSum)
      
  except:
    break