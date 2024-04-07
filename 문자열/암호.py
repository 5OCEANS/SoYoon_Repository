import sys

word = sys.stdin.readline().rstrip()

key = sys.stdin.readline().strip()

scretWord = ''

# 유니코드를 이용해 보기.
# 일단 키를 평문의 길이보다 길게 늘리기.
if len(word) > len(key):
  num = 0
  if len(word) % len(key) != 0:
    num = int(len(word) // len(key)) + 1
  else:
    num = int(len(word) // len(key))
  
  key = num * key

for i in range(len(word)):
  if word[i].isspace():
    scretWord += ' '
  else:
    scretchr = ord(word[i]) - ord(key[i]) + 96
    if scretchr < 97:
      scretWord += chr(122 - (97 - scretchr) + 1)
    else:
      scretWord += chr(scretchr)

print(scretWord)