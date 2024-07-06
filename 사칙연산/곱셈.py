import sys

firstNum = int(sys.stdin.readline().strip())
secondNum = sys.stdin.readline().strip()

three = firstNum * int(secondNum[2])
four = firstNum * int(secondNum[1])
five = firstNum * int(secondNum[0])

six = three + four * 10 + five * 100

print(three)
print(four)
print(five)
print(six)