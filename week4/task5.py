"""
https://leetcode.com/problems/container-with-most-water/submissions/1421399668/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            diff = right - left
            area = min(height[left], height[right]) * diff
            maxarea = max(maxarea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
