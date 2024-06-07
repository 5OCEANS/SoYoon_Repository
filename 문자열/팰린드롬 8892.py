import sys

T = int(sys.stdin.readline())

for i in range(T):
  k = int(sys.stdin.readline())
  wordList = []
  count = 0

  for j in range(k):
    word = sys.stdin.readline().strip()
    wordList.append(word)

  for j in range(len(wordList)): # 첫 번째 단어 0 1 2 3 4
    for k in range(len(wordList)): # 붙일 단어 # 0 1 2 3 4
      if j == k:
        continue
      else:
        combinedString = wordList[j] + wordList[k]
        # 길이가 홀수인 경우 7 -> index 3
        # 중심을 찾고 중심 이전의 string과 중심 이후의 string이 같은지 보면 된다.
        if len(combinedString) % 2 != 0:
          center = len(combinedString) // 2
          if combinedString[0:center] == combinedString[center+1:][::-1]:
            print(combinedString)
            count += 1
            break
          else:
            continue

        # 길이가 짝수인 경우
        else:
          center = len(combinedString) // 2
          if combinedString[0:center] == combinedString[center:][::-1]:
            print(combinedString)
            count += 1
            break
          else:
            continue
    if count > 0:
      break
  else:
    print(0)
  