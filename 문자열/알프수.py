import sys

X = list(sys.stdin.readline().strip())

pos = 10
neg = 10

past = int(X[0])

for i in range(1, len(X)):
  if i == 1 and int(X[1]) - past < 0:
    print('NON ALPSOO')
    break
  if i == len(X)-1 and int(X[i]) - past > 0:
    print('NON ALPSOO')
    break
  if past == int(X[i]):
    # print('기울기가 0일 때')
    print('NON ALPSOO')
    break
  elif past > int(X[i]):
    if neg != 10: # 기울기가 음수가 된 것이 처음이 아닐 때. 예전의 기울기와 비교해야 함.
      if (past - int(X[i])) != neg:
        # print('기울기가 음수가 된 것이 처음이 아닐 때. 예전의 기울기와 비교해야 함.')
        print('NON ALPSOO')
        break
      else:
        past = int(X[i])
        continue
    else: # 기울기가 음수가 된 것이 처음일 때. neg 기울기를 초기화해야 함.
      neg = past - int(X[i])
      past = int(X[i])
      pos = 10
      continue
  else:
    if pos != 10: # 기울기가 양수가 된 것이 처음이 아닐 때. 예전의 기울기와 비교해야 함.
      if (int(X[i]) - past) != pos:
        # print('기울기가 양수가 된 것이 처음이 아닐 때. 예전의 기울기와 비교해야 함.')
        # print(pos, int(X[i]) - past, int(X[i]), past)
        print('NON ALPSOO')
        break
      else:
        past = int(X[i])
        continue
    else: # 기울기가 양수가 된 것이 처음일 때. pos 기울기를 초기화해야 함.
      pos = int(X[i]) - past
      past = int(X[i])
      neg = 10
      continue
else:
  print('ALPSOO')