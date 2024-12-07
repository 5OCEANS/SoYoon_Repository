import sys

T = int(sys.stdin.readline())
for i in range(T):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  if (numList[0]*numList[1]) > (numList[2]*numList[3]):
    print('TelecomParisTech')
  elif (numList[0]*numList[1]) < (numList[2]*numList[3]):
    print('Eurecom')
  else:
    print('Tie')