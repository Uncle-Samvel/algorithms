'''
https://leetcode.com/problems/valid-palindrome/description/
'''


def check(s: str) -> bool:
    answer = ''
    for char in s.lower():
        if char.isalnum():
            answer += char

    return True if answer == answer[::-1] else False
