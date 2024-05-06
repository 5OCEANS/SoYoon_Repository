import sys

count = 0

while True:
  try:

    string = sys.stdin.readline().strip()
    print(string)

    count += 1

    if count >= 100:
      break

  except:
    break