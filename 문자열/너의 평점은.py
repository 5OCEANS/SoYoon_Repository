import sys

def score(grade):
  if grade == 'A+':
    return 4.5
  elif grade == 'A0':
    return 4.0
  elif grade == 'B+':
    return 3.5
  elif grade == 'B0':
    return 3.0
  elif grade == 'C+':
    return 2.5
  elif grade == 'C0':
    return 2.0
  elif grade == 'D+':
    return 1.5
  elif grade == 'D0':
    return 1.0
  elif grade == 'F':
    return 0.0
  elif grade == 'P':
    return -30.0

totalScore = 0.0
cnt = 0

for i in range(20):
  subject, credit, grade = sys.stdin.readline().strip().split()

  subjectScore = score(grade)

  if int(subjectScore) == -30:
    continue
  
  cnt += int(round(float(credit)))
  totalScore += float(credit) * subjectScore

print(totalScore/ cnt)