'''
https://contest.yandex.ru/contest/45468/problems/17/
'''

first = list(map(int, input().split()))
second = list(map(int, input().split()))
counter = 0

while len(first) != 0 and len(second) != 0 and counter < 1000000:
    if first[0] > second[0] and (first[0] != 9 or second[0] != 0) or (first[0] == 0 and second[0] == 9):
        first.append(first[0])
        first.append(second[0])
        first.pop(0)
        second.pop(0)
    elif first[0] < second[0] and (first[0] != 0 or second[0] != 9) or (first[0] == 9 and second[0] == 0):
        second.append(first[0])
        second.append(second[0])
        first.pop(0)
        second.pop(0)
    counter += 1

if len(first) == 0:
    print('second', counter)
elif len(second) == 0:
    print('first', counter)
elif counter == 1000000:
    print('botva')
