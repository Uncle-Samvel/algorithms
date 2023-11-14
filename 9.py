'''
https://contest.yandex.ru/contest/28730/problems/D/
'''

amount = int(input())

data = [int(x) for x in input().split()]
sum = sum(data)

if (sum % amount) / amount >= 0.5:
    ans = sum//amount + 1
else:
    ans = sum//amount

print(ans)