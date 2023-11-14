'''
https://contest.yandex.ru/contest/50668/problems/?nc=0hY00I8G
'''

num = int(input())
rezult = []

for i in range(num):
    data = input().split(',')
    param_1 = len(set(data[0] + data[1] + data[2]))
    param_2 = (sum(map(int,list(data[3]))) + sum(map(int,list(data[4])))) * 64
    param_3 = (ord(data[0].lower()[0]) - ord('a') + 1) * 256
    x = ('000' + hex(param_1 + param_2 + param_3)[2:])[-3:]
    rezult.append(x.upper())

print(*rezult)

