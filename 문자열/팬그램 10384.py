import sys

n = int(sys.stdin.readline())
cnt = 1

for i in range(n):
  alphaDic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J':0, 'K': 0,
            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
  
  string = sys.stdin.readline().strip()
  string = string.upper()

  for j in range(len(string)):
    if string[j].isalpha():
      alphaDic[string[j]] += 1

  isPangram = ''

  if min(list(alphaDic.values())) == 0:
    isPangram = 'Not a pangram'    
  elif min(list(alphaDic.values())) == 1:
    isPangram = 'Pangram!'
  elif min(list(alphaDic.values())) == 2:
    isPangram = 'Double pangram!!'
  else:
    isPangram = 'Triple pangram!!!'

  print('Case ' + str(cnt) + ': ' + isPangram)

  cnt += 1