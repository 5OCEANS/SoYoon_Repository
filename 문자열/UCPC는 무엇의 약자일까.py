import sys

string = sys.stdin.readline().strip()
answer = ''

for i in range(len(string)):
  if string[i].isupper():
    answer += string[i]


index = 0

for i in range(len(answer)):
  if index == 0 and answer[i] == 'U':
    index += 1
  elif index == 1 and answer[i] == 'C':
    index += 1
  elif index == 2 and answer[i] == 'P':
    index += 1
  elif index == 3 and answer[i] == 'C':
    index += 1
  if index == 4:
    print('I love UCPC')
    break
else:
  print('I hate UCPC')
