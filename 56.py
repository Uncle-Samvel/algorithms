'''
https://contest.yandex.ru/contest/29150/problems/B/
'''

str = input()
flag = False
result = []

for i in range(len(str) - 1):
    if str[i] == str[i + 1]:
        result += [str[i:i + 2]]
        flag = True

if flag == False:
    for i in range(len(str) - 2):
        if str[i] == str[i + 2]:
            result += [str[i:i + 3]]
            flag = True
if flag == False:
    print(-1)
else:
    print(min(result))

