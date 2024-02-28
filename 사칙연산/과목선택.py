import sys

scienceList = [int(sys.stdin.readline().strip()) for _ in range(4)]
socialList = [int(sys.stdin.readline().strip()) for _ in range(2)]

scienceList.remove(min(scienceList))
socialList.remove(min(socialList))

print(sum(scienceList)+sum(socialList))