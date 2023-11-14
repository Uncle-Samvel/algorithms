'''
стажка задача №1
'''

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = list(map(int, input().split()))
stop = list(map(int, input().split()))

StartDay = 365 * start[0] * 86400 + sum(month[:start[1] - 1]) * 86400 + start[2] * 86400 + start[3] * 3600 + start[4] * 60 + start[5]
StopDay = 365 * stop[0] * 86400 + sum(month[:stop[1] - 1]) * 86400 + stop[2] * 86400 + stop[3] * 3600 + stop[4] * 60 + stop[5]

print((StopDay - StartDay)//86400, (StopDay - StartDay) % 86400)
