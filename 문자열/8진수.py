import sys

N = sys.stdin.readline().strip()

N = N[::-1]

octNum = ''

j = 0

while j < len(N):
  string = ''
  if j+3 <= len(N):
    string = N[j:j+3]
  else:
    string = N[j:]
  
  string = string[::-1]

  if int(string) == 0:
    octNum += '0'
  elif int(string) == 1:
    octNum += '1'
  elif int(string) == 10:
    octNum += '2'
  elif int(string) == 11:
    octNum += '3'
  elif int(string) == 100:
    octNum += '4'
  elif int(string) == 101:
    octNum += '5'
  elif int(string) == 110:
    octNum += '6'
  elif int(string) == 111:
    octNum += '7'
  
  j += 3

octNum = octNum[::-1]

print(octNum)