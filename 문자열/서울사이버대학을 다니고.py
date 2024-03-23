import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

set_string = set(string)

set_string.discard(' ')
set_string.discard(',')
set_string.discard('.')

string_num = []

for i in set_string:
  string_num.append(string.count(i))

print(max(string_num))