# https://leetcode.com/problems/binary-tree-inorder-traversal/
from utils import *

Solution.args(root=[1,None,2,3])

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFS(Solution):
    def solve(self, root: TreeNode | None):
        res = []

        def dfs(root: TreeNode | None):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        return res

DFS()

Solution.analyze()