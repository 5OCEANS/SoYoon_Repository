import sys

# ljes=njak
# lj, e, s=, nj, a, k

string = sys.stdin.readline().strip()

index = 0
cnt = 0
while index < len(string):
  if string[index:index+2] == 'c=' or string[index:index+2] == 'c-':
    cnt += 1
    index += 2
    continue
  elif string[index:index+3] == 'dz=':
    cnt += 1
    index += 3
    continue
  elif string[index:index+2] == 'd-':
    cnt += 1
    index += 2
    continue
  elif string[index:index+2] == 'lj':
    cnt += 1
    index += 2
    continue
  elif string[index:index+2] == 'nj':
    cnt += 1
    index += 2 
    continue 
  elif string[index:index+2] == 's=':
    cnt += 1
    index += 2  
    continue  
  elif string[index:index+2] == 'z=':
    cnt += 1
    index += 2  
    continue
  else:
    cnt += 1
    index += 1

print(cnt)