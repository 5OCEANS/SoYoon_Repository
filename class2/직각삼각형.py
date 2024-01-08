while(True):
  try:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
      break

    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)

    maxNum = max(numList)

    maxNumIndex = numList.index(maxNum)
    notMaxNumIndextList = []
    for i in range(0, 3):
      if i == maxNumIndex:
        continue
      else:
        notMaxNumIndextList.append(i)

    if maxNum**2 == numList[notMaxNumIndextList[0]]**2 + numList[notMaxNumIndextList[1]]**2:
      print("right")
    else:
      print("wrong")
  
  except:
    break