'''
https://contest.yandex.ru/contest/29188/problems/
'''

size = int(input())
data = sorted(list(map(int,input().split())))
amount = int(input())
rezult = []

for i in range(amount):
    search = list(map(int,input().split()))
    if data[0] <= search[0] <= data[-1] or data[0] <= search[1] <= data[-1]:
        left = 0
        right = len(data) - 1
        while left < right:
            medium = (right + left) // 2
            if data[medium] >= search[0]:
                right = medium
            else:
                left = medium + 1
        rezult.append(-left)

        left = 0
        right = len(data) - 1
        while left < right:
            medium = (right + left + 1) // 2
            if data[medium] <= search[1]:
                left = medium
            else:
                right = medium - 1

        rezult[-1] += (right + 1)
    else:
        rezult.append(0)
print(*rezult)






