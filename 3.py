'''
Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a != 0:
    if c != 0 and -b / a == -d / c:
        print('NO')
    else:
        if b % a == 0:
            print(-b // a)
        else:
            print('NO')

elif a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')