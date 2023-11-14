'''
https://contest.yandex.ru/contest/28964/problems/B/
'''

a = [int(x) for x in input().split()]
dict_a = {}
for x in a:
    if x in dict_a:
        print("YES")
    else:
        print("NO")
        dict_a[x] = 1