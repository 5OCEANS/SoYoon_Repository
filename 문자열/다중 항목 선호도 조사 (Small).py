# ver 1

import sys

n, m = map(int, sys.stdin.readline().strip().split())

studentPreferenceList = []
question = []

for i in range(n):
  studentPreference = list(sys.stdin.readline().strip().split())
  studentPreferenceList.append(studentPreference)

for i in range(m):
  q = list(sys.stdin.readline().strip().split())
  question.append(q)

for i in range(m): # 질의 개수
  result = {} # 학생들이 질의와 동일한지

  for e in range(n):
    result[e] = True

  for k in range(n): # 검사해야 하는 학생 인원
    for j in range(3): # 학생 한 명의 과목, 과일, 색깔
      if question[i][j] == '-':
        continue
      elif question[i][j] != studentPreferenceList[k][j]:
        result[k] = False
        break
  
  print(list(result.values()).count(True))


# ver 2

import sys

n, m = map(int, sys.stdin.readline().strip().split())

studentPreferenceList = []
question = []

for i in range(n):
  studentPreference = list(sys.stdin.readline().strip().split())
  studentPreferenceList.append(studentPreference)

for i in range(m):
  q = list(sys.stdin.readline().strip().split())
  question.append(q)

  result = {} # 학생들이 질의와 동일한지

  for e in range(n):
    result[e] = True

  for k in range(n): # 검사해야 하는 학생 인원
    for j in range(3): # 학생 한 명의 과목, 과일, 색깔
      if q[j] == '-':
        continue
      elif q[j] != studentPreferenceList[k][j]:
        result[k] = False
        break
  
  print(list(result.values()).count(True))