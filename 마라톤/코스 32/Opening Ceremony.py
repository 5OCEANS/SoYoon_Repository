import sys

K = int(sys.stdin.readline())
for i in range(K):
  c, n = map(int, sys.stdin.readline().strip().split()) # 참가국 수, 개막식에 참가한 선수 수
  registerList = list(map(int, sys.stdin.readline().strip().split())) # 각 나라의 총 등록 선수 수
  participateList = list(map(int, sys.stdin.readline().strip().split())) # 개막식에 참가한 선수들의 소속 국가 정보

  absenceList = list()
  for j in range(c):
    absenceList.append(registerList[j]-participateList.count(j+1))
  print('Data Set %d:' %(i+1))
  print(max(absenceList))
  print()