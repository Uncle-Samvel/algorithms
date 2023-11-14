'''
https://contest.yandex.ru/contest/28964/problems/C/
'''

a = [int(x) for x in input().split()]
dict_a = {}

for x in a:
    if x in dict_a:
        dict_a[x] += 1
    else:
        dict_a[x] = 1

for x in dict_a:
    if dict_a[x] == 1:
        print(x,end=' ')

