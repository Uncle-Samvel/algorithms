'''
https://contest.yandex.ru/contest/28736/problems/C/
'''


def neighbour(x, y, data):
    Neighbour = 0
    for example in data:
        if abs(x - example[0]) == 1 and y == example[1]:
            Neighbour += 1
        elif abs(y - example[1]) == 1 and x == example[0]:
            Neighbour += 1
    return Neighbour


data = []
amount = int(input())
sum = 0
for i in range(amount):
    example = [int(x) for x in input().split()]
    number = neighbour(example[0], example[1], data)
    if number == 0:
        sum += 4
    elif number == 1:
        sum += 2
    elif number == 3:
        sum -= 2
    data += [example]

print(sum)
