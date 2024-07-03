# problem url: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        q, seen = deque([root]), set()

        while q:
            cur = q.popleft()
            if cur.val in seen:
                return True
            else:
                seen.add(k - cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return False

