import sys

a = float(sys.stdin.readline().strip())
galon = 3.785411784
mile = 1.609344

print(100/(mile/galon*a))