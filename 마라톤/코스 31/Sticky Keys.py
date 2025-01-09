def remove_consecutive_duplicates(s):
  result = []
  prev_char = None 

  for char in s:
    if char != prev_char:  
      result.append(char)
      prev_char = char  

  return ''.join(result)  

import sys
s = sys.stdin.readline().rstrip()

print(remove_consecutive_duplicates(s))