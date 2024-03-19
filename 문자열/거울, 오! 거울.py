# import sys

# while True:
#   try:
#     sentence = str(sys.stdin.readline().strip())

#     if sentence == '***':
#       break

#     reversed_sentence = sentence[::-1] 
#     print(reversed_sentence)

#   except Exception as e:
#     print(e)
#     break

while True:
  a = input()
  if a == "***":
    break
  else:
    print(a[::-1])