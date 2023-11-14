'''
https://contest.yandex.ru/contest/8458/problems/?utm_source=habr&utm_content=post070519&nc=YmwLNciU
'''

s1 = input()
s2 = input()
s1_set = set(s1)

sum = 0
for i in s2:
    if i in s1_set:
        sum += 1

print(sum)
