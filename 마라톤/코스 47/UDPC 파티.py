import sys

V = sys.stdin.readline().strip()
U = D = P = C = 0
Answer = ""

for ch in V:
  if ch == 'U':
    U += 1
    C += 1
  elif ch == 'C':
    U += 1
    C += 1
  else:
    P += 1
    D += 1

if D % 2 == 0:
  if U > (D // 2):
    Answer += "U"
else:
  if U > (D // 2) + 1:
    Answer += "U"

if D > 0:
  Answer += "D"
  Answer += "P"

if Answer == "":
  Answer += "C"

print(Answer)