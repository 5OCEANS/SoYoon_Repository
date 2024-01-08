cnt = int(input())
inputString = list(input())
alphabetList = 'abcdefghijklmnopqrstuvwxyz'
resHash = 0

for i in range(len(inputString)):
  resHash += (alphabetList.index(inputString[i]) + 1) * 31**i

print(resHash % 1234567891)