'''
https://contest.yandex.ru/contest/8458/problems/C/
'''


amount = int(input())
if amount != 0:
    value = int(input())
    print(value)

for i in range(amount - 1):
    value_last = value
    value = int(input())
    if value != value_last:
        print(value)
