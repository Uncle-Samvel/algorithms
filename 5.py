'''
Могла ли такая ситуация быть при игре в крестики-нолики

1. когда больше одной выигрышной прямой
2. когда кол-во 1 больше кол-ва 2 на число большее 1
'''

def check_amount(game):
    amount_1 = 0
    amount_2 = 0
    for i in range(3):
        for j in range(3):
            if game[i][j] == 1:
                amount_1 += 1
            elif game[i][j] == 2:
                amount_2 += 1
    if amount_1 - amount_2  == 1:
        return(1)
    if amount_1 - amount_2 == 0:
        return(2)
    else:
        return(0)

def check_column(game):
    res_1 = 0
    res_2 = 0
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] == 1:
            res_1 += 1
        elif game[0][i] == game[1][i] == game[2][i] == 2:
            res_2 += 1
    res = res_1 + res_2
    if res > 1:
        return(0)
    elif res_1 == 1:
        return(1)
    elif res_2 == 1:
        return(2)
    else:
        return(3)

def check_line(game):
    res_1 = 0
    res_2 = 0
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 1:
            res_1 += 1
        elif game[i][0] == game[i][1] == game[i][2] == 2:
            res_2 += 1
    res = res_1 + res_2
    if res > 1:
        return(0)
    elif res_1 == 1:
        return(1)
    elif res_2 == 1:
        return(2)
    else:
        return(3)


def check_diagonal(game):
    res_1 = 0
    res_2 = 0
    if game[0][0] == game[1][1] == game[2][2] == 1:
        res_1 += 1
    elif game[0][2] == game[1][1] == game[2][0] == 1:
        res_1 += 1
    elif game[0][0] == game[1][1] == game[2][2] == 2:
        res_2 += 1
    elif game[0][2] == game[1][1] == game[2][0] == 2:
        res_2 += 1
    if res_2 == 1:
        return(2)
    elif res_1 == 1:
        return(1)
    else:
        return(0)

game = []
for i in range(3):
    game += [[int(x) for x in input().split()]]

if check_amount(game) == 0  or  check_column(game)  == 0 or check_line(game)  == 0:
    print('NO')
elif (check_column(game)  == 2 or check_line(game)  == 2 or check_diagonal(game) == 2) and check_amount(game) != 2:
    print('NO')
elif (check_column(game)  == 1 or check_line(game)  == 1 or check_diagonal(game) == 1) and check_amount(game) != 1:
    print('NO')
else:
    print('YES')






