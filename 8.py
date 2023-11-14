'''
https://contest.yandex.ru/contest/28730/problems/E/
'''


def dist(x,y,X,Y):
    return(((X-x)**2 + (Y-y)**2)**0.5)

d = int(input())
cord = [float(x) for x in input().split()]

if cord[1] + cord[0] - d <= 0 and cord[1] >= 0 and cord[0] >= 0:
    print(0)
else:
    res = [[1,dist(0,0,cord[0],cord[1])],
           [2,dist(d,0,cord[0],cord[1])],
           [3,dist(0,d, cord[0], cord[1])]]
    res.sort(key=lambda x: x[1])

    print(res[0][0])
