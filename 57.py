'''
https://contest.yandex.ru/contest/29150/problems/C/
'''


amount = int(input())
targets = []
flag = 'YES'

for i in range(amount):
    target = list(map(int,input().split()))
    if len(target) == 4:
        targets.append([target[2] * 2,target[3] * 2])
    else:
        targets.append([(target[1] + target[5]), (target[2] + target[6])])

if amount < 3:
    print('YES')
else:
    old = [targets[1][0] - targets[0][0],targets[1][1] - targets[0][1]]
    b = [targets[1][0],targets[1][1]]
    targets = targets[2:]
    for new in targets:
        if old[0] * (new[1] - b[1]) - old[1] * (new[0] - b[0]) != 0:
            flag = 'NO'
    print(flag)


