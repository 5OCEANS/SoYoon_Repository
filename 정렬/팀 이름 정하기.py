import sys 

name = list(sys.stdin.readline().strip())

N = int(sys.stdin.readline())

scoreList = []

for i in range(N):
  teamName = list(sys.stdin.readline().strip())

  L = name.count('L') + teamName.count('L')
  O = name.count('O') + teamName.count('O')
  V = name.count('V') + teamName.count('V')
  E = name.count('E') + teamName.count('E')

  score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

  scoreList.append((score, teamName))

scoreList.sort(key=lambda x : (-x[0], x[1]))

for i in range(len(scoreList[0][1])):
  print(scoreList[0][1][i], end='')