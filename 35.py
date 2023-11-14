'''
https://contest.yandex.ru/contest/29396/problems/C/
'''
x = int(input())

events = []
start = 1
stop = 1
flag = False
result = []

while 1:
    events.append([start, stop])
    start, stop = map(int, input().split())
    if start == 0 and stop == 0:
        break

events = events[1:]
events.sort()

lastStart = -100000000
lastStop = -1000000

for event in events:
    if event[0] <= 0 <= event[1] and event[1] > lastStop:
        lastStart = event[0]
        lastStop = event[1]
        flag = True

example = [lastStart, lastStop]

lastNewStart = lastStart
lastNewStop = lastStop

if flag == True:
    result = [[lastStart, lastStop]]
    for event in events:

        if result[-1][1] >= x:
            break

        if lastStart <= event[0] <= lastStop and event[1] > lastNewStop:
            lastNewStart = event[0]
            lastNewStop = event[1]
            example = event

        if event[0] > lastStop and lastNewStart <= event[0] <= lastNewStop:
            result += [example]
            lastStart = lastNewStart
            lastStop = lastNewStop
            example = []
            if event[1] > lastStop:
                lastNewStart = event[0]
                lastNewStop = event[1]
                example = event

        if event == events[-1] and example != [] and example not in result and result[-1][1] < x:
            result += [example]

    if result[-1][1] >= x:
        print(len(result))
        for i in result:
            print(*i)
    else:
        print("No solution")
else:
    print("No solution")

