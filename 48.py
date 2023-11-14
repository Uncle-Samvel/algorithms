'''
https://contest.yandex.ru/contest/8458/problems/B/
'''

amount = int(input())
counter = 0
maxCounter = 0

for i in range(amount):
    x = int(input())
    if x == 1:
        counter += 1
        maxCounter = max(counter, maxCounter)
    else:
        counter = 0
print(maxCounter)
