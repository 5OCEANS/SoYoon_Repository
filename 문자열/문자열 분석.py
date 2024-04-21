import sys

while True:
  string = sys.stdin.readline().rstrip('\n')

  if not string:
    break

  lowerCnt = 0
  upperCnt = 0
  numberCnt = 0
  spaceCnt = 0

  for i in string:
    if i.isspace():
      spaceCnt += 1
    elif i.isnumeric():
      numberCnt += 1
    elif i.isupper():
      upperCnt += 1
    elif i.islower():
      lowerCnt += 1
    
  print(lowerCnt, upperCnt, numberCnt, spaceCnt)