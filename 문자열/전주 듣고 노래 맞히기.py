import sys

N, M = map(int, sys.stdin.readline().strip().split())

titleList = []
soundList = []

for i in range(N):
  string = sys.stdin.readline().strip().split()
  T = int(string[0])
  titleList.append(string[1])
  soundList.append(str(string[2:5]))

for i in range(M):
  searchSound = str(sys.stdin.readline().strip().split())

  if searchSound in soundList:
    if soundList.count(searchSound) > 1:
      print('?')
    else:
      print(titleList[soundList.index(searchSound)])
  else:
    print('!')
