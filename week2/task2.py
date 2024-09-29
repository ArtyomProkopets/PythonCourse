"""
https://leetcode.com/problems/next-greater-element-iii/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def nextGreaterElement(self, n):
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums = nums[: i + 1] + sorted(nums[i + 1 :])
        result = int("".join(nums))
        return result if result < 2**31 else -1
