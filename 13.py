'''
https://contest.yandex.ru/contest/28736/problems/A/
'''

x = [int(x) for x in input().split()]
data = [int(x) for x in input().split()]
print(max(data) - min(data))
