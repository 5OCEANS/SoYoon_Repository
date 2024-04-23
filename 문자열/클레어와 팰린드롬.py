import sys

a = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
lst = list(string)

for i in range(a):
  if lst[i] == '?' and lst[::-1][i] != '?':
    lst[i] = lst[::-1][i]
  elif lst[i] == '?' and lst[::-1][i] == '?':
    lst[i] = 'a'
print(''.join(lst))


input()
s=input()
for i,j in zip(s,s[::-1]):print(end=max(i,j,'a'))