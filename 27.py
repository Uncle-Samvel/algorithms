'''
https://contest.yandex.ru/contest/50668/problems/B/
'''

num = int(input())

key = []
log = {}

for i in range(num):
    data = input().split()
    if int(data[3]) not in log:
        key.append(int(data[3]))
        if data[4] == 'C':
            log[int(data[3])] = int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2])
        elif data[4] == 'S':
            log[int(data[3])] = int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2])
        elif data[4] == 'A':
            log[int(data[3])] = -(int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2]))
        else:
            log[int(data[3])] = 0

    else:
        if data[4] == 'C':
            log[int(data[3])] += (int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2]))
        elif data[4] == 'S':
            log[int(data[3])] += (int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2]))
        elif data[4] == 'A':
            log[int(data[3])] -= (int(data[0]) * 24 * 60 + int(data[1]) * 60 + int(data[2]))

key.sort()

for i in key:
    print(log[i],end=' ')














