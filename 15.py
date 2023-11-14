'''
https://contest.yandex.ru/contest/28964/problems/A/
'''

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(len(set(a) & set(b)))