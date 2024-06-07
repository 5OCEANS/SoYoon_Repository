import sys

n = int(sys.stdin.readline())
birthdateDic = {}

for i in range(n):
  name, day, month, year = sys.stdin.readline().strip().split()

  birthdate = year + (month if len(month) == 2 else ('0'+month)) + day

  birthdateDic[birthdate] = name

birthdateSort = sorted(list(birthdateDic.keys()))

print(birthdateDic[birthdateSort[-1]])
print(birthdateDic[birthdateSort[0]])