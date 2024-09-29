"""
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
