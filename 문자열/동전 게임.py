import sys

P = int(sys.stdin.readline())

for i in range(P):
  play = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0,
          'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
  
  playList = sys.stdin.readline().strip()
  
  for j in range(38):
    string = playList[j:j+3]

    play[string] += 1
  
  # print(' '.join(str(num) for num in play.values()))
  print(*list(play.values()))