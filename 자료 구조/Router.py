import sys

N = int(sys.stdin.readline())
buffer = []

while True:
  try:
    info = int(sys.stdin.readline())

    if info == -1:
      if len(buffer) != 0:
        print(' '.join(buffer))
        break
      else:
        print('empty')
        break

    if info == 0 and len(buffer) != 0:
      buffer.pop(0)
    elif info != 0 and len(buffer) < N:
      buffer.append(str(info))

  except:
    break