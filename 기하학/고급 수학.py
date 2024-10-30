import sys

for i in range(int(sys.stdin.readline())):
  s=sorted(list(map(int,sys.stdin.readline().strip().split())))
  print('Scenario #{}:'.format(i+1))
  if s[0]**2 + s[1]**2 == s[2]**2:  
    print("yes\n")
  else:
    print("no\n")