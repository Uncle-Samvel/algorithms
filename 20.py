'''https://contest.yandex.ru/contest/28970/problems/A/'''

amount = int(input())
result = {}

for i in range(amount):
    example = [int(x) for x in input().split()]
    if example[0] in result:
        result[example[0]] += example[1]
    else:
        result[example[0]] = example[1]

for i in sorted(result):
    print(i,result[i])