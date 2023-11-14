'''
https://contest.yandex.ru/contest/8458/problems/E/
'''

s1 = input()
s2 = input()
dict_1 = {}
dict_2 = {}

for i in s1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1

for i in s2:
    if i not in dict_2:
        dict_2[i] = 1
    else:
        dict_2[i] += 1

if dict_1 == dict_2:
    print(1)
else:
    print(0)
