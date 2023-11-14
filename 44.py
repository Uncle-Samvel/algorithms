'''
https://leetcode.com/problems/permutation-in-string/description/
'''


def search(s1: str, s2: str) -> bool:
    dict_1 = {}
    dict_2 = {}
    for i in s1:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1

    index_1 = 0
    index_2 = len(s1)

    for i in s2[:index_2]:
        if i not in dict_2:
            dict_2[i] = 1
        else:
            dict_2[i] += 1

    if dict_1 == dict_2:
        return True
    else:
        for i in range(index_2,len(s2)):
            if s2[i] not in dict_2:
                dict_2[s2[i]] = 1
            else:
                dict_2[s2[i]] += 1
            if dict_2[s2[index_1]] > 1:
                dict_2[s2[index_1]] -= 1
            else:
                dict_2.pop(s2[index_1])
            if dict_1 == dict_2:
                return True
            index_1 += 1
        return False


print(search('ab', 'bewt'))
