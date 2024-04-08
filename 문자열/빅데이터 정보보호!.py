import sys

N = int(sys.stdin.readline())

stringList = sys.stdin.readline().strip()
security = 0
bigdata = 0

for i in range(N):
  if stringList[0] == 's':
    stringList = stringList[8:]
    security += 1
  elif stringList[0] == 'b':
    stringList = stringList[7:]
    bigdata += 1
  
if security > bigdata:
  print('security!')
elif security < bigdata:
  print('bigdata?')
else:
  print('bigdata? security!')