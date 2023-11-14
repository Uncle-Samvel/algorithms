'''
стажка задача №2
'''

data = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dict_A = {}
dict_B = {}


for i in A:
    if i in dict_A:
        dict_A[i] += 1
    else:
        dict_A[i] = 1

for i in B:
    if i in dict_B:
        dict_B[i] += 1
    else:
        dict_B[i] = 1

for i in dict_A:
    if i in dict_B:
        x = min(dict_B[i],dict_A[i])
        dict_B[i] -= x
        dict_A[i] -= x

result = sum(dict_A[x] for x in dict_A)
result += sum(dict_B[x] for x in dict_B)


for i in range(data[2]):
    new = input().split()
    new[0] = int(new[0])
    new[2] = int(new[2])
    if new[0] == 1:
        if new[1] == 'A':
            if new[2] in dict_B and dict_B[new[2]] > 0:
                dict_B[new[2]] -= 1
                result -= 1
            else:
                if new[2] in dict_A and dict_A[new[2]] > 0:
                    dict_A[new[2]] += 1
                else:
                    dict_A[new[2]] = 1
                result += 1
        elif new[1] == 'B':
            if new[2] in dict_A and dict_A[new[2]] > 0:
                dict_A[new[2]] -= 1
                result -= 1
            else:
                if new[2] in dict_B and dict_B[new[2]] > 0:
                    dict_B[new[2]] += 1
                else:
                    dict_B[new[2]] = 1
                result += 1
    elif new[0] == -1:
        if new[1] == 'A':
            if new[2] in dict_A and dict_A[new[2]] > 0 :
                dict_A[new[2]] -= 1
                result -= 1
            else:
                if new[2] in dict_B and dict_B[new[2]] > 0:
                    dict_B[new[2]] += 1
                else:
                    dict_B[new[2]] = 1
                result += 1
        elif new[1] == 'B':
            if new[2] in dict_B and dict_B[new[2]] > 0:
                dict_B[new[2]] -= 1
                result -= 1
            else:
                if new[2] in dict_A and dict_A[new[2]] > 0:
                    dict_A[new[2]] += 1
                else:
                    dict_A[new[2]] = 1
                result += 1

    print(result,end=' ')
