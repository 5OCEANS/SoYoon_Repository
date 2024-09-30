import sys

while True:
  try:
    string = sys.stdin.readline().strip()
    if string == '*':
      break

    for i in range(len(string)-1):
      charSet = set()
      for j in range(len(string)-i-1):
        pair = string[j] + string[i+j+1]
        if pair in charSet:
          print(string + " is NOT surprising.")
          isSurprising = False
          break
        else:
          charSet.add(pair)
      else:
        continue
      break
    else:
      print(string, "is surprising.")

  except:
    break
