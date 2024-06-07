import sys

string = sys.stdin.readline().strip()

index = 0
ansList = []

while index < len(string):
  if string[index].isupper() and string[index: index+7] == 'What is':
    ans = ''
    while string[index] != '?':
      if string[index] == '.':
        break
      ans += string[index]
      index += 1
    else:
      ans = ans.replace('What', 'Forty-two')
      ans += '.'
      ansList.append(ans)
    index += 1

  else:
    index += 1

for i in range(len(ansList)):
  print(ansList[i])