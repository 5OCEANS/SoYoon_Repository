import sys

while True:
  try:
    num = float(sys.stdin.readline().strip())
    if int(num) == -1:
      break
    print('Objects weighing %0.2f on Earth will weigh %0.2f on the moon.' %(num, num*0.167))

  except:
    break