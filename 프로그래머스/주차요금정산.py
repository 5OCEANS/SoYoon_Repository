def solution(fees, records):
    from collections import defaultdict

    def chkTime(inT, out):  # "05:34", "08:30"
        inHour, inMin = map(int, inT.split(':'))
        outHour, outMin = map(int, out.split(':'))
        inTime = inHour * 60 + inMin
        outTime = outHour * 60 + outMin
        return (outTime - inTime)

    def calculMoney(time):  # 178
        money = 0
        if fees[0] >= time:
            money = fees[1]
        else:
            money += fees[1]
            time -= fees[0]
            money += ((time // fees[2]) if time % fees[2] == 0 else ((time // fees[2]) + 1)) * fees[3]
        return money

    answer = []
    carDict = dict()  # "5961" : "05:34"
    carTimeDict = defaultdict(int)  # "5961": 180 (분)

    for i in range(len(records)):
        if records[i].split()[2] == 'OUT':
            time = chkTime(carDict[records[i].split()[1]], records[i].split()[0])
            carTimeDict[records[i].split()[1]] += time
            carDict[records[i].split()[1]] = ""
        else:
            carDict[records[i].split()[1]] = records[i].split()[0]
    for key, val in carDict.items():  # 0이 아닌 값을 확인
        if val != "":
            time = chkTime(val, "23:59")
            carTimeDict[key] += time
    sortedCarTimeDict = sorted(carTimeDict.items(), key=lambda x: x[0])
    for key, val in sortedCarTimeDict:
        money = calculMoney(val)
        answer.append(money)

    return answer