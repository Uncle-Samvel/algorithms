'''
RLE aaabbbbcccc => 3a4b4c
'''


num = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


def search(chars):
    number = 0
    value = ''
    ans = []
    value = chars[0]

    for i in range(len(chars)):
        if chars[i] != value:
            ans.append(value)
            if number > 1:
                ans.append(str(number))
            value = chars[i]
            number = 1

        else:
            number += 1

        if i == (len(chars) - 1):
            if chars[i] != value:
                ans.append(value)
                if number > 1:
                    ans.append(str(number))
                ans.append(chars[i])
            else:
                ans.append(value)
                if number > 1:
                    ans.append(str(number))
    return list(''.join(ans))

print(search(num))