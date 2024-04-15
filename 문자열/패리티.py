import sys

while True:
  try:
    string = sys.stdin.readline().strip()
    cnt1 = 0

    if string == '#':
      break

    if string[-1] == 'e':
      for i in string:
        if i == '1':
          cnt1 += 1
      if cnt1 % 2 == 0:
        string = string[:-1] + '0'
      else:
        string = string[:-1] + '1'
      
      print(string)
      
    elif string[-1] == 'o':
      for i in string:
        if i == '1':
          cnt1 += 1
      if cnt1 % 2 == 0:
        string = string[:-1] + '1'
      else:
        string = string[:-1] + '0'
      print(string)

  except:
    break