import sys

n = int(sys.stdin.readline())

for i in range(n):
  string = sys.stdin.readline().strip()
  print_string = ''

  print('String #', end = '')
  print(i+1)

  for j in range(len(string)):
    ord_num = ord(string[j])

    if ord_num == 90:
      ord_num = 64

    print_string += chr(ord_num+1)
  
  print(print_string)

  print()