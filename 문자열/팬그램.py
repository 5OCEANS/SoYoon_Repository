import sys

while True:
  try:
    
    list = [0] * 26

    string = sys.stdin.readline().strip()

    if string == '*':
      break

    for i in string:
      if i.isalpha():
        list[ord(i)-97] = 1
    
    if sum(list) == 26:
      print('Y')
    else:
      print('N')


  except:
    break