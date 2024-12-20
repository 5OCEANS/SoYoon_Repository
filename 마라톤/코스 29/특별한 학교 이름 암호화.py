import sys

def move_one_ord(schoolName):
  for i in range(10):
    if schoolName[i] >= ord('z'):
      schoolName[i] = ord('a')
    else:
      schoolName[i] += 1
  return schoolName

def check_school_name(schoolName):
  global NLCS
  global BHA
  global KIS
  global SJA
  for i in range(10):
    if NLCS[i] != schoolName[i]:
      break
  else:
    return 'NLCS'
  for i in range(10):
    if BHA[i] != schoolName[i]:
      break
  else:
    return 'BHA'
  for i in range(10):
    if KIS[i] != schoolName[i]:
      break
  else:
    return 'KIS'
  for i in range(10):
    if SJA[i] != schoolName[i]:
      break
  else:
    return 'SJA'
  return 'NONE'


NLCS = [ord(i) for i in 'northlondo']
BHA = [ord(i) for i in 'branksomeh']
KIS = [ord(i) for i in 'koreainter']
SJA = [ord(i) for i in 'stjohnsbur']
schoolName = [ord(i) for i in list(sys.stdin.readline().strip())]
for i in range(26):
  ans = check_school_name(schoolName)
  if ans == 'NONE':
    move_one_ord(schoolName)
  else:
    print(ans)
    break