import sys

N = int(sys.stdin.readline())

peopleDic = {}

for k in range(N):
  for i in range(4):
    work = sys.stdin.readline().strip().split()

    sumNum = 0

    if i % 2 == 0: # 4시간 근무
      sumNum = 4
    elif i == 1: # 6시간 근무
      sumNum = 6
    else:
      sumNum = 10
    
    for j in range(len(work)):
      if work[j] == '-':
        continue
      else:
        if work[j] in peopleDic:
          peopleDic[work[j]] += sumNum
        else:
          peopleDic[work[j]] = sumNum

if not peopleDic:
  print('Yes')
else:

  maxTime = max(peopleDic.values())
  minTime = min(peopleDic.values())

  if maxTime - minTime <= 12:
    print('Yes')
  else:
    print('No')