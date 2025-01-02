import sys

count = 1
while True:
  try:
    L = int(sys.stdin.readline().strip())
    if L == 0:
      break
    print('User', count)
    count += 1
    N = int(sys.stdin.readline())
    for i in range(N):
      numberOfSteps = int(sys.stdin.readline().strip())
      print('%0.5f' %(L*numberOfSteps/100000))

  except:
    break