'''
https://contest.yandex.ru/contest/29396/problems/A/
'''

amountLine = int(input())
events = []
result = 0
counter = 0

for i in range(amountLine):
    open, close = map(int, input().split())
    events.append([open, 1])
    events.append([close, -1])

events.sort()

start = events[0][0]

for event in events:
    if counter > 0:
        result += (event[0] - start)
    start = event[0]
    counter += event[1]


print(result)

