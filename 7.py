'''
вам даётся запись некоторой корректной даты. Требуется выяснить, однозначно ли по этой записи определяется дата даже без дополнительной информации о формате
'''
date = [int(x) for x in input().split()]
if date[0] <= 12 and date[1] <= 12 and date[0] != date[1]:
    print(0)
else:
    print(1)