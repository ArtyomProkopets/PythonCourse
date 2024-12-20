"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        arr = [root]
        while len(arr) > 0:
            capacity = len(arr)
            cur_level = []
            for _ in range(capacity):
                tek_elem = arr[0]
                del arr[0]
                cur_level += [tek_elem.val]

                if tek_elem.left:
                    arr += [tek_elem.left]
                if tek_elem.right:
                    arr += [tek_elem.right]
            answer += [cur_level]
        return answer
