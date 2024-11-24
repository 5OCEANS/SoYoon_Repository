import sys

while True:
  try:
    n, k = map(int, sys.stdin.readline().strip().split())
    result = n  
    stamps = n  

    while stamps >= k:
      new_chickens = stamps // k  
      result += new_chickens  
      stamps = stamps % k + new_chickens  
    print(result)
  except:
    break
