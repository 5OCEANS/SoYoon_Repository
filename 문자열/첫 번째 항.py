import sys

cnt = 1

while True:
  try:
    string = sys.stdin.readline().strip()
    result = ''

    if string == '0':
      break

    prev = string

    while result == '':
      tmpString = ''

      if len(string) % 2 != 0:
        result = string
        break

      for i in range(0, len(string), 2):
        if i + 3 < len(string):
          if string[i+1] == string[i+3]:
            result = string
            break
        tmpString += int(string[i]) * string[i+1]
      else:
        string = tmpString
        if prev == string:
          result = string
          break
        else:
          prev = string
      
    print('Test ' + str(cnt) + ': ' + result)
    cnt += 1

  except Exception as e:
    print(e)
    break

# 312211
# 111221
# 1211
# 21
# 11
# 1