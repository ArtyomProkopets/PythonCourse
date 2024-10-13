"""
https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        result = 0
        sign = 1
        i = 0
        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1
        for char in s[i:]:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        num = sign * result
        INT_MIN, INT_MAX = -2147483648, 2147483647
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        return num
