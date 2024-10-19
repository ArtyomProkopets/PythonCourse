"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len