import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
  title, minutes = sys.stdin.readline().strip().split(',')
  minutes = int(minutes)
  print(title+' - ', end='')
  if minutes >= 365*24*60:
    print(str(minutes // (365*24*60)) + ' year(s) ', end ='')
    minutes = minutes % (365*24*60)
  if minutes >= 24*60:
    print(str(minutes//(24*60))+' day(s) ', end='')
    minutes = minutes % (24*60)
  if minutes >= 60:
    print(str(minutes//60) + ' hour(s) ', end='')
    minutes = minutes % (60)
  if minutes < 60:
    print(str(minutes)+' minute(s)')