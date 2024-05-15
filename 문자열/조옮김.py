import sys

while True:
  try:
    soundList = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    string = sys.stdin.readline().strip()
    
    if string  == '***':
      break

    stringList = string.split()

    n = int(sys.stdin.readline())

    for i in range(len(stringList)):
      if stringList[i] not in soundList:
        if 'b' in stringList[i]:
          stringList[i] = soundList[(soundList.index(stringList[i][0]) + n - 1) % 12]
        else:
          stringList[i] = soundList[(soundList.index(stringList[i][0]) + n + 1) % 12]
      else: 
        stringList[i] = soundList[(soundList.index(stringList[i]) + n) % 12]

    print(' '.join(stringList))
  except:
    break