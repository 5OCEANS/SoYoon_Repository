import sys

N = int(sys.stdin.readline())
friendsList = []

friendsList = list(sys.stdin.readline().strip().split())

eliceTrack = sys.stdin.readline().strip()

num = friendsList.count(eliceTrack)

print(num)