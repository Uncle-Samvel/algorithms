'''
https://contest.yandex.ru/contest/28736/problems/D/
'''

x = int(input())
data = [int(x) for x in input().split()]
data.sort()
max = data[-1]
if max <= (sum(data) - max):
    print(sum(data))
else:
    print(2*max - sum(data))