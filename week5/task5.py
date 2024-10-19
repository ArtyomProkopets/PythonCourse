"""
https://leetcode.com/problems/bulls-and-cows/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])
        return "{}A{}B".format(bulls, cows)
