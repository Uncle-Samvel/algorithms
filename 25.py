'''
https://contest.yandex.ru/contest/29075/problems/E/
'''
import sys

flag = 1
sum = int(input())

num_1 = list(map(int, input().split()))
num_2 = list(map(int, input().split()))
num_3 = list(map(int, input().split()))


num_1 = num_1[1:]
num_2 = num_2[1:]
num_3 = num_3[1:]

set_num_3 = set(num_3)

for i in range(len(num_1)):
    for j in range(len(num_2)):
        if (sum - num_1[i] - num_2[j]) in set_num_3:
            print(i,j,num_3.index(sum - num_1[i] - num_2[j]))
            sys.exit()


print(-1)
