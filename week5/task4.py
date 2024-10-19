"""
https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        return list(repeated)
