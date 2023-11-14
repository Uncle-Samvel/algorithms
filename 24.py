'''
https://contest.yandex.ru/contest/29075/problems/D/
'''

arr = input()
flag = 0
flag_2 = 0
for i in arr:
    if i == '(':
        flag += 1
    else:
        flag -= 1
    if flag < 0:
        flag_2 = 1
        print('NO')
        break

if flag == 0:
    print('YES')
elif flag != 0 and flag_2 != 1:
    print('NO')