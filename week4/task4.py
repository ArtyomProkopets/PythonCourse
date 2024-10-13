"""
https://leetcode.com/problems/reverse-string/?envType=problem-list-v2&envId=string&status=SOLVED
"""


class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
