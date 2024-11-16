import sys

visitingT, visitingF, visitingS, visitingP, visitingC = map(int, sys.stdin.readline().strip().split())
homeT, homeF, homeS, homeP, homeC = map(int, sys.stdin.readline().strip().split())

visitiongTotalScore = 6*visitingT + 3*visitingF + 2*visitingS + 1*visitingP + 2*visitingC
hoemTotalScore = 6*homeT + 3*homeF + 2*homeS + 1*homeP + 2*homeC

print(visitiongTotalScore, hoemTotalScore)