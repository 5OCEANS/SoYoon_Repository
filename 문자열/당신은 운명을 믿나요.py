import sys

S = sys.stdin.readline().strip()

YONSEI = 'YONSEI'
KOREA = 'KOREA'

yonseiNum = 0
koreaNum = 0

for i in range(len(YONSEI)):
  yonseiNum = S.find(YONSEI[i], yonseiNum)

  if yonseiNum == -1:
    break

for i in range(len(KOREA)):
  koreaNum = S.find(KOREA[i], koreaNum)

  if koreaNum == -1:
    break

if yonseiNum != -1 and koreaNum != -1:
  if yonseiNum > koreaNum:
    print('KOREA')
  else:
    print('YONSEI')
else:
  print('YONSEI') if yonseiNum != -1 else print('KOREA')