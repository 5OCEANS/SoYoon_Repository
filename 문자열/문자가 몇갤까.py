import sys

while True:
  try:
    string = sys.stdin.readline().strip()

    if string == '#':
      break

    list = [0] * 26

    for i in string.lower():
      if i.isalpha():
        list[ord(i)-97] = 1
      else:
        continue

    print(list.count(1)) # 1의 개수 출력

  except:
    break