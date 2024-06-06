'''
Найти символ который повторяется чаще всего
'''

s = input()
max = 0
max_2 = 0
dict = {}

for i in s:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

for key in dict:
    if dict[key] > max:
        max = dict[key]
        max_2 = key

print(max,max_2)
