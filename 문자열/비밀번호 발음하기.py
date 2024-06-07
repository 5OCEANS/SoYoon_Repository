import sys

while True:
  try:
    string = sys.stdin.readline().strip()

    if string == 'end':
      break

    if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
      pass
    else:
      print('<' + string + '> is not acceptable.')
      continue

    prev = string[0]
    vowelCnt = 0 if string[0] not in 'aeiou' else 1 # 모음이 연속적으로 몇 개인지
    consonantCnt = 0 if vowelCnt != 0 else 1 # 자음이 연속적으로 몇 개인지

    for i in range(1, len(string)):
      if prev == string[i]:
        if string[i] not in 'eo':
          print('<' + string + '> is not acceptable.')
          break
      prev = string[i]
      if string[i] in 'aeiou':
        vowelCnt += 1
        consonantCnt = 0
      else:
        consonantCnt += 1
        vowelCnt = 0
      
      if vowelCnt > 2 or consonantCnt > 2:
        print('<' + string + '> is not acceptable.')
        break
    else:
      print('<' + string + '> is acceptable.')
      
  except:
    break