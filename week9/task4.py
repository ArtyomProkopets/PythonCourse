"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/distribute-coins-in-binary-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans += abs(left) + abs(right)
            return node.val + left + right - 1

        ans = 0
        dfs(root)
        return ans
