import sys

N, S = sys.stdin.readline().strip().split()

chatNameList = []
chatMsgList = []

cnt = 0

for i in range(int(N)):
  name, message = sys.stdin.readline().strip().split()
  chatNameList.append(name)
  chatMsgList.append(message)

order = chatNameList.index(S)

for i in range(order):
  if chatMsgList[i] == chatMsgList[order]:
    cnt += 1
  
print(cnt)