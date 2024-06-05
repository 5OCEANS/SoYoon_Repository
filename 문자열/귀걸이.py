import sys

scenario = 1

while True:
  try:
    n = int(sys.stdin.readline())
    if n == 0:
      break

    nameList = []

    for i in range(n):
      name = sys.stdin.readline().strip()
      nameList.append(name)

    numList = []

    for i in range(2*n-1):
      num, alphabet = sys.stdin.readline().strip().split()
      numList.append(int(num))

    for i in range(n):
      if numList.count(i+1) == 1:
        print(scenario, nameList[i])  
        scenario += 1

  except:
    break