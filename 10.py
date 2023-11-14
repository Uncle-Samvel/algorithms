'''
https://contest.yandex.ru/contest/28730/problems/B/
'''

data = [int(x) for x in input().split()]
if data[1] > data[2]:
    data[1], data[2] = data[2], data[1]
d1 = abs(data[2] - data[1]) - 1
d2 = data[1] + (data[0] - data[2]) - 1
print(min(d1, d2))
