import sys

commanddic = dict()
penalty = 0
completeProblem = 0

while True:
  command = sys.stdin.readline().strip()

  if command == '-1':
    break

  if command.split()[2] == 'right':
    if command.split()[1] in commanddic.keys():
      penalty += int(command.split()[0])
      penalty += (commanddic[command.split()[1]] * 20)
      completeProblem += 1
    else:
      penalty += int(command.split()[0])
      completeProblem+= 1
  else:
    if command.split()[1] in commanddic.keys():
      commanddic[command.split()[1]] += 1
    else:
      commanddic[command.split()[1]] = 1
    
print(completeProblem, penalty)


