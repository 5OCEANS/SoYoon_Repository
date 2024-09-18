import sys

while True:
  try:
    inputsentence = sys.stdin.readline().strip()
    remove_set = {' '}

    if inputsentence == 'END':
      break

    inputset = set(inputsentence) 
    inputset.discard(' ')
    inputsentenceExceptSpacing = [i for i in inputsentence if i not in remove_set]

    if len(inputset) == len(inputsentenceExceptSpacing):
      print(inputsentence)

  except:
    break