import sys, decimal

context = decimal.getcontext()              # 파이썬 반올림함수 round 오류 해결 방법
context.rounding = decimal.ROUND_HALF_UP

string = sys.stdin.readline().strip()

H = string.count('H')
A = string.count('A')
P = string.count('P')
Y = string.count('Y')

S = string.count('S')
D = string.count('D')

happyScore = H + A + P + Y
sadScore = S + A + D

happinessIndex = (happyScore / (happyScore + sadScore)) * 100 if happyScore + sadScore != 0 else 0.5 * 100

happinessIndexRound = float(decimal.Decimal(str(happinessIndex)).quantize(decimal.Decimal("1.00")))

print('%0.2f'%happinessIndexRound)