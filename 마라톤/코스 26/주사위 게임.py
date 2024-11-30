import sys

a1, b1, a2, b2 = map(int, sys.stdin.readline().strip().split())
firstDiceTotalScore = sum([i for i in range(a1, b1+1)]) / (b1-a1+1)
secondDiceTotalScore = sum([i for i in range(a2, b2+1)]) / (b2-a2+1)
goongAvgScore = firstDiceTotalScore + secondDiceTotalScore

a1, b1, a2, b2 = map(int, sys.stdin.readline().strip().split())
firstDiceTotalScore = sum([i for i in range(a1, b1+1)]) / (b1-a1+1)
secondDiceTotalScore = sum([i for i in range(a2, b2+1)]) / (b2-a2+1)
seokAvgScore = firstDiceTotalScore + secondDiceTotalScore

if goongAvgScore > seokAvgScore:
  print('Gunnar')
elif goongAvgScore < seokAvgScore:
  print('Emma')
else:
  print('Tie')


# 쉬운 소스코드
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))

print("Gunnar" if a>b else "Emma" if a<b else "Tie")