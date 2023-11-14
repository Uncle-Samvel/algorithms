'''
стажка задача №3
'''

size = list(map(int, input().split()))
data = []
name = input().split()
dict_name_2 = {}
dict_name = {}
sum_item = []

for i in range(len(name)):
    dict_name[name[i]] = [-100000000000, 100000000000]
    dict_name_2[name[i]] = i

for i in range(size[0]):
    c = list(map(int, input().split()))
    data = data + c
    sum_item.append(sum(c))

sumData = sum(sum_item)

for i in range(size[2]):
    request = input().split()
    request[2] = int(request[2])

    if request[1] == '<':
        dict_name[request[0]][1] = min(dict_name[request[0]][1], request[2])

    elif request[1] == '>':
        dict_name[request[0]][0] = max(dict_name[request[0]][0], request[2])

flag = True

for i in dict_name:
    if dict_name[i][0] >= dict_name[i][1]:
        flag = False
print(dict_name)

if flag == False:
    print(0)

elif flag == True:
    delets = set()

    for i in dict_name:

        if dict_name[i][0] < min(data) and dict_name[i][1] > max(data):
            continue

        for j in range(dict_name_2[i], len(data), len(name)):
            if dict_name[i][0] >= data[j] or dict_name[i][1] <= data[j]:
                delets.add(j // len(name))


    for delet in delets:
        sumData -= sum_item[delet]

    print(sumData)