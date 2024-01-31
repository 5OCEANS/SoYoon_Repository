firstList = []
secondList = []

for _ in range(3):
    P, Y, S = input().split()
    firstList.append(int(Y))
    secondList.append([int(P), S])

firstList.sort()
secondList.sort(reverse=True)

first_teamName = ""
second_teamName = ""

for i in range(3):
    first_teamName += str(firstList[i] % 100)
    second_teamName += secondList[i][1][0]

print(first_teamName)
print(second_teamName)