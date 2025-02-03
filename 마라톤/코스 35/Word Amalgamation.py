import sys

wordDict = {}

while True:
  word = sys.stdin.readline().strip()
  if word == "XXXXXX":
    break
  sortedWord = ''.join(sorted(word)) 
  if sortedWord in wordDict:
    wordDict[sortedWord].append(word)
  else:
    wordDict[sortedWord] = [word]

while True:
  scrambledWord = sys.stdin.readline().strip()
  if scrambledWord == "XXXXXX":
    break
  sortedScrambledWord = ''.join(sorted(scrambledWord))  
  if sortedScrambledWord in wordDict:
    for word in sorted(wordDict[sortedScrambledWord]):  
      print(word)
  else:
    print("NOT A VALID WORD")
  
  print("******") 
