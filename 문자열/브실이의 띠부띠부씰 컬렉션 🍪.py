import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

BCnt = string.count('B')
RCnt = string.count('R') // 2
OCnt = string.count('O')
NCnt = string.count('N')
ZCnt = string.count('Z')
ECnt = string.count('E') // 2
SCnt = string.count('S')
ICnt = string.count('I')
LCnt = string.count('L')
VCnt = string.count('V')

print(min(BCnt, RCnt, OCnt, NCnt, ZCnt, ECnt, SCnt, ICnt, LCnt, VCnt))