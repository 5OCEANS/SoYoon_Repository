import sys

while True:
  try:
    line = list(sys.stdin.readline().strip().split())
    chr = line[0]
    string = str(line[1:]).lower()

    if chr == '#':
      break

    cnt = string.count(chr.lower())

    print(chr, cnt)

  except:
    break