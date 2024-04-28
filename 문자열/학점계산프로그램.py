import sys

S = sys.stdin.readline().strip()
totalScore = 0.0
subjectCnt = 0

while True:
  try:

    i = 1
    
    if i < len(S) and S[i] == '+':
      i += 1

    score = S[0:i]

    if score == 'A+':
      totalScore += 4.5
      subjectCnt += 1

    elif score == 'A':
      totalScore += 4.0
      subjectCnt += 1

    elif score == 'B+':
      totalScore += 3.5
      subjectCnt += 1

    elif score == 'B':
      totalScore += 3.0
      subjectCnt += 1

    elif score == 'C+':
      totalScore += 2.5
      subjectCnt += 1

    elif score == 'C':
      totalScore += 2.0
      subjectCnt += 1

    elif score == 'D+':
      totalScore += 1.5
      subjectCnt += 1

    elif score == 'D':
      totalScore += 1.0
      subjectCnt += 1

    elif score == 'F':
      subjectCnt += 1
        
    if S[i] == None:
      break 

    S = S[i:]

  except:
    break

print(totalScore/subjectCnt)




a=input()
s,x=0,0
for i in a:
    if i=='+': s+=0.5
    else:
        x+=1
        if i=='A': s+=4.0
        elif i=='B': s+=3.0
        elif i=='C': s+=2.0
        elif i=='D': s+=1.0
print(s/x)