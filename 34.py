'''
https://contest.yandex.ru/contest/29396/problems/B/
'''

amountEvent = int(input())
events = []
counter = 0
maxCounter = 0

for i in range(amountEvent):
    start, duration = map(int,input().split())
    events.append([start,1])
    events.append([start + duration,-1])

events.sort()

for event in events:
    counter += event[1]
    maxCounter = max(maxCounter,counter)

print(maxCounter)

