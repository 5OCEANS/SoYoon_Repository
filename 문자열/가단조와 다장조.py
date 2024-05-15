import sys

soundList = sys.stdin.readline().strip().split('|')
firstsound = []
minor = 0
major = 0

for i in range(len(soundList)):
  if soundList[i][0] in ['A', 'D', 'E']:
    minor += 1
  elif soundList[i][0] in ['C', 'F', 'G']:
    major += 1

if minor > major:
  print('A-minor')
elif minor < major:
  print('C-major')
else:
  lastsound = soundList[len(soundList) - 1][-1]

  if lastsound in ['A', 'D', 'E']:
    print('A-minor')
  else:
    print('C-major')