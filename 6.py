'''
Среди треугольников периметра P с целыми длинами сторон найдите треугольник наибольшей и наименьшей ненулевой площади.
'''

perimeter = int(input())
if perimeter == 4:
    print(-1)

elif perimeter % 3 == 0:
    print(perimeter//3,perimeter//3,perimeter//3 )
    if (perimeter - 1) % 2 == 0:
        print(1,(perimeter - 1)//2,(perimeter - 1)//2)
    else:
        print(2, (perimeter - 2) // 2, (perimeter - 2) // 2)
elif perimeter % 3 == 1:
    print(perimeter//3,perimeter//3,perimeter//3 + 1 )
    if (perimeter - 1) % 2 == 0:
        print(1,(perimeter - 1)//2,(perimeter - 1)//2)
    else:
        print(2, (perimeter - 2) // 2, (perimeter - 2) // 2)
elif perimeter % 3 == 2:
    print(perimeter//3,perimeter//3 + 1,perimeter//3 + 1 )
    if (perimeter - 1) % 2 == 0:
        print(1,(perimeter - 1)//2,(perimeter - 1)//2)
    else:
        print(2, (perimeter - 2) // 2, (perimeter - 2) // 2)
