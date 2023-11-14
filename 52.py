'''
https://leetcode.com/problems/merge-intervals/
'''

intervals = [[1, 4], [4, 5]]


def search(intervals: list[list[int]]) -> list[list[int]]:
    events = []

    result = []

    for i in intervals:
        events.append([i[0], -1])
        events.append([i[1], 1])
    events.sort()
    start = events[0][0]
    stop = events[0][0]
    lens = len(events)

    counter = 0

    for i in range(lens):
        if events[i][1] == -1:
            counter += 1
        elif events[i][1] == 1:
            counter -= 1
        if counter == 0:
            stop = events[i][0]
            result.append([start, stop])
            start = events[(i + 1) % lens][0]

    return result


print(search(intervals))
