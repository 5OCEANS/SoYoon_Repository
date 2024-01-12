k = int(input())
numList = [0]
sum = 0

for i in range(k):
  n = int(input())
  if n == 0:
    sum -= numList[-1]
    numList.pop()
  else:
    sum += n
    numList.append(n)

print(sum)