'''
https://contest.yandex.ru/contest/28970/problems/B/
'''

result = {}

for i in range(int(input())):
    example = [x for x in input().split()]
    if example[0] in result:
        result[example[0]] += int(example[1])
    else:
        result[example[0]] = int(example[1])
for i in sorted(result):
    print(i, result[i])
