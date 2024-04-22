# 런타임 에러

# import sys

# k, slen = map(int, sys.stdin.readline().split())

# string = sys.stdin.readline().strip()
# newString = ''

# for i in range(slen):
#   if string[i].isalpha():

#     newChrOrd = ord(string[i]) + k

#     if string[i].isupper():
#       if newChrOrd > 90:  # 91 -> 65 92 -> 66
#         newChrOrd -= 26
#     else:
#       if newChrOrd > 122:  # 123 -> 97 124 -> 98
#         newChrOrd -= 26
#     newString += chr(newChrOrd) 

#   else:
#     newString += string[i]

# print(newString)

import sys

k, slen = map(int, sys.stdin.readline().split())

string = sys.stdin.readline().strip()
newString = ''

for ch in string:
  if ch.isalpha():
    shift = k % 26
    if ch.isupper():
      encrypted_ord = ord('A') + (ord(ch) - ord('A') + shift) % 26
    else:
      encrypted_ord = ord('a') + (ord(ch) - ord('a') + shift) % 26
    newString += chr(encrypted_ord)
  else:
    newString += ch

print(newString)