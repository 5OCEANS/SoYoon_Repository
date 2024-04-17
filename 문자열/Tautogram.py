import sys

while True:
  try:
    stringList = list(sys.stdin.readline().strip().split())
    firstchr = stringList[0][0].lower()
    
    if firstchr == '*':
      break

    for i in (stringList):
      if firstchr != i[0].lower():
        print('N')
        break
    else:
      print('Y')        

  except:
    break

