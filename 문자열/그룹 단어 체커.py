import sys

N = int(sys.stdin.readline())

result = 0

for i in range(N):
  string = sys.stdin.readline().strip()

  alphabetList = []
  alphabetList.append(string[0])
  prev = string[0]

  for j in range(1, len(string)):
    if prev == string[j]:
      continue
    else:
      if string[j] not in alphabetList:
        alphabetList.append(string[j])
        prev = string[j]
      else:
        break
  else:
    result += 1

print(result)