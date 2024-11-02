import sys, math

L = int(sys.stdin.readline().strip())
height = math.sqrt(L**2 - (L*0.5)**2)

print(L*height*0.5)