# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p and q:
                print(f"{p.val}, {q.val}")
                if p.val != q.val:
                    return False
                else:
                    result = True and dfs(p.left, q.left) and  dfs(p.right, q.right)
                    return result
            if not p and not q:
                return True
            return False
        
        return dfs(p,q)

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and  p.val == q.val:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
        else:
            return False
        