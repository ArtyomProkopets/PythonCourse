"""
https://leetcode.com/problems/group-anagrams/submissions/1427506022/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())
