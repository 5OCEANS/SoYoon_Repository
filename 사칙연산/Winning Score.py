import sys

apples = 0

for i in range(3):
  num = int(sys.stdin.readline())
  apples += (num) * (3-i)

bananas = 0

for i in range(3):
  num = int(sys.stdin.readline())
  bananas += (num) * (3-i)

if apples > bananas:
  print('A')
elif apples < bananas:
  print('B')
else:
  print('T')

