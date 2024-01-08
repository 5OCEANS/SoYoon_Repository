while(True):
  try:
    numList = []
    numList = list(map(int, input()))
    if numList == [0]:
      break

    centerNum = len(numList)//2

    ifPass = True
    for i in range(0, centerNum):
      if numList[i] != numList[len(numList) -1 -i]:
        print("no")
        ifPass = False
        break
    if ifPass:
      print("yes")

  except:
    break