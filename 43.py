'''
https://leetcode.com/problems/generate-parentheses/solutions/2542620/
'''


def leetcode(n: int) -> list[str]:
    def generate(s, open, close, index, n, result) -> list[str]:

        if index <= (2 * n - 1):
            if open == close:
                s[index] = '('
                a = generate(s, open + 1, close, index + 1, n, result)
                return a
            elif open == n:
                s[index] = ')'
                b = generate(s, open, close + 1, index + 1, n, result)
                return b
            elif 0 < open < n:
                s[index] = '('
                a = generate(s, open + 1, close, index + 1, n, result)
                s[index] = ')'
                b = generate(s, open, close + 1, index + 1, n, result)
                return a, b
        else:
            result.append(''.join(s))

    s = 2 * n * ['1']
    result = []
    generate(s, 0, 0, 0, n, result)
    return result
