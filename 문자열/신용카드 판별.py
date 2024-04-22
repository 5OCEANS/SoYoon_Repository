import sys

T = int(sys.stdin.readline())

for k in range(T):
  cardNum = sys.stdin.readline().strip()
  sum = 0

  for i in range(len(cardNum)):
    if i % 2 != 0: # 홀수 번째 수       16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
      sum += int(cardNum[i])
    else:
      num = 2 * int(cardNum[i])

      if num >= 10:
        num = str(num)
        numSum = 0
        for j in num:
          numSum += int(j)
        num = numSum
      
      sum += num
  
  if sum % 10 == 0:
    print('T')
  else:
    print('F')