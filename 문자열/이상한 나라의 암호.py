import sys

num = 1

while True:
  try:
    string = sys.stdin.readline().strip()

    if string == 'Was it a cat I saw?':
      break

    cnt = 0

    while len(string) > cnt:

      print(string[cnt], end = '')

      cnt += (num + 1)

    print()

    num += 1

  except:
    break
