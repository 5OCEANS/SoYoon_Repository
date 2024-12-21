import sys
cat = ''

for i in range(15):
  string = list(sys.stdin.readline().strip().split())
  if 'w' in string:
    cat = 'chunbae'
  elif 'b' in string:
    cat = 'nabi'
  elif 'g' in string:
    cat = 'yeongcheol'

print(cat)