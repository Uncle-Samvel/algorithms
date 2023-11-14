'''
https://leetcode.com/problems/maximize-distance-to-closest-person/description/
'''

seats = [1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]


def search(seats: list[int]) -> int:
    maxCounter = 0
    counter = 0
    start = 0
    stop = 0
    for i in range(len(seats)):
        if seats[i] == 0:
            counter += 1
            maxCounter = max(counter, maxCounter)
        if seats[i] == 1:
            counter = 0
    return max((maxCounter + 1) // 2, seats.index(1),seats[::-1].index(1))


print(search(seats))
