# 암호화하는 과정
import sys

def moveChar(char, count):
  charOrd = 0
  if ord(char) + count > ord('Z'):
    charOrd = ord('A') + (count - ord('Z') + ord(char) - 1)
  else:
    charOrd = ord(char) + count
  return chr(charOrd)


K = int(sys.stdin.readline())
stringList = list(sys.stdin.readline().strip())
for i in range(len(stringList)):
  count = 3 * (i+1) + K
  print(moveChar(stringList[i], count), end='')
print()

# 암호화된 단어를 해독하는 코드
import sys

def moveChar(char, count):
  ansChrOrd = 0
  if ord(char) - count < ord('A'):
    ansChrOrd = ord('Z') - (count - (ord(char) - ord('A') + 1))
  else:
    ansChrOrd = ord(char) - count
  return chr(ansChrOrd)


K = int(sys.stdin.readline())
stringList = list(sys.stdin.readline().strip())
for i in range(len(stringList)):
  count = 3 * (i+1) + K
  print(moveChar(stringList[i], count), end='')
print()