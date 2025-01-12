import sys

count = 1
while True:
  try:
    line = sys.stdin.readline().strip()
    if line == '0':
      break
    n, s = line.split()

    priority = {char : idx for idx, char in enumerate(s)}
    strings = [sys.stdin.readline().strip() for _ in range(int(n))]
    
    strings.sort(key= lambda word: [priority[char] for char in word]) # ANTLER는 [0, 13, 19, 11, 4, 17]로 변환
    
    print('year %d' %(count))
    count += 1
    for string in strings:
      print(string)
  except:
    break