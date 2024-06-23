import sys

N = int(sys.stdin.readline().strip())
pattern = sys.stdin.readline().strip().split('*')

for i in range(N):
  string = sys.stdin.readline().strip()
  if len(string) < (len(pattern[0]) + len(pattern[1])):
    print('NE')
    continue
    
  if string[0:len(pattern[0])] == pattern[0] and string[-1*(len(pattern[1])):] == pattern[1]:
    print('DA')
  else:
    print('NE')