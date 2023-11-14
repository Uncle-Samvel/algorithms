'''
По координатам 4 точек, определить является ли фигура параллелограмом
'''


def angle(x_1, y_1, x_2, y_2):
    if x_1 == x_2:
        return ('inf')
    else:
        return ((y_2 - y_1) / (x_2 - x_1))


number = int(input())

for i in range(number):
    res = 0
    coord = [int(x) for x in input().split()]
    if angle(coord[0], coord[1], coord[2], coord[3]) == angle(coord[4], coord[5], coord[6], coord[7]):
        res += 1
    if angle(coord[0], coord[1], coord[4], coord[5]) == angle(coord[2], coord[3], coord[6], coord[7]):
        res += 1
    if angle(coord[0], coord[1], coord[6], coord[7]) == angle(coord[2], coord[3], coord[4], coord[5]):
        res += 1
    if res == 2:
        print('YES')
    if res != 2:
        print('NO')
