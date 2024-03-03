import sys

n = 0

while(True):
  try:
    num = int(sys.stdin.readline())
    if num == -1:
      print(n)
      break
    n += num
  except:
    break