'''
https://contest.yandex.ru/contest/28964/problems/D/
'''

num = int(input())
command = input()
ans_yes = set()
ans_no = set()

while command != "HELP":
    a = set(int(x) for x in command.split())
    answer = input()
    if answer == 'NO' and len(ans_yes) == 0:
        ans_no.update(a)
    elif answer == 'NO' and len(ans_yes) != 0:
        ans_yes -= a
    elif answer == 'YES' and len(ans_yes) != 0:
        ans_yes = ans_yes & a
    else:
        ans_yes.update(a)
    command = input()
    if len(ans_yes) != 0:
        ans_yes -= ans_no
        ans_no.clear()

if len(ans_yes) == 0:
    for i in range(1, num + 1):
       if i not in ans_no:
           print(i)
else:
    print(*sorted(ans_yes))
