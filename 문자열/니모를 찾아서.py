import sys

while True:
  try:

    string = sys.stdin.readline().strip()

    if string == 'EOI':
      break

    if 'nemo' in string.lower():
      print('Found')
    else:
      print('Missing')

  except:
    break