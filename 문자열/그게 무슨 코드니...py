a=input()
print('CE' if a[0]!='"' or a[-1]!='"' or len(a)<3 else eval(a))