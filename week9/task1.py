"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def RecurseValid(cur_node, left=float("-inf"), right=float("inf")):
            if not cur_node:
                return True
            if not (left < cur_node.val < right):
                return False

            return RecurseValid(cur_node.left, left, cur_node.val) and RecurseValid(
                cur_node.right, cur_node.val, right
            )

        return RecurseValid(root)
