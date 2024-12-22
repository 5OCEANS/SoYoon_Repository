import sys

def grade(score):
  if score >= 97:
    return 'A+'
  elif score >= 90:
    return 'A'
  elif score >= 87:
    return 'B+'
  elif score >= 80:
    return 'B'
  elif score >= 77:
    return 'C+'
  elif score >= 70:
    return 'C'
  elif score >= 67:
    return 'D+'
  elif score >= 60:
    return 'D'
  else:
    return 'F'


n = int(sys.stdin.readline())
for _ in range(n):
  name, score = sys.stdin.readline().strip().split()
  print(name, grade(int(score)))