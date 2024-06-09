import sys

hDic = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve'}
mDic = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve',
        '13': 'thirteen', '14': 'fourteen', '15': 'quarter', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty one', '22': 'twenty two',
        '23': 'twenty three', '24': 'twenty four', '25': 'twenty five', '26': 'twenty six', '27': 'twenty seven', '28': 'twenty eight', '29': 'twenty nine', '30': 'half'}

h = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()

if int(m) == 0:
  print(hDic[h] + ' o\' clock')
elif int(m) <= 30:
  if int(m) == 15 or int(m) == 30:
    print(mDic[m] + ' past ' + hDic[h])
  elif int(m) == 1:
    print(mDic[m] + ' minute' + ' past ' + hDic[h])
  else:
    print(mDic[m] + ' minutes' + ' past ' + hDic[h])
else:
  if int(m) == 45:
    print(mDic['15'] + ' to ' + hDic[str((int(h) + 1)%12 if (int(h) + 1)%12 != 0 else 12)])
  elif int(m) == 59:
    print(mDic[str(60 - int(m))] + ' minute to ' + hDic[str((int(h) + 1)%12 if (int(h) + 1)%12 != 0 else 12)])
  else:
    print(mDic[str(60 - int(m))] + ' minutes to ' + hDic[str((int(h) + 1)%12 if (int(h) + 1)%12 != 0 else 12)])

