'''
https://leetcode.com/problems/group-anagrams/
'''

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dict = {}
    result = []
    for word in strs:
        new = ''.join(sorted(word))
        if new not in dict:
            dict[new] = [word]
        else:
            dict[new].append(word)
    for key in dict:
        result.append(dict[key])
    return result