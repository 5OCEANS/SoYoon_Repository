import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  soundList = list(sys.stdin.readline().strip().split())

  while True:
    string = list(sys.stdin.readline().strip().split())
    if string == ['what', 'does', 'the', 'fox', 'say?']:
      break
    
    for j in range(soundList.count(string[2])):
      soundList.remove(string[2])
    
  print(' '.join(soundList))

