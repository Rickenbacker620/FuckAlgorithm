# https://leetcode.com/problems/count-complete-tree-nodes/
from utils import *

Solution.args(6, root=tree_constructor([1,2,3,4,5,6]))
Solution.args(0, root=tree_constructor([]))
Solution.args(1, root=tree_constructor([1]))
Solution.args(4, root=tree_constructor([1,2,3,4]))
Solution.args(5, root=tree_constructor([1,2,3,4,5]))


# FIXME this cannot be solved using DFS
class DFS(Solution):
    def solve(self, root):

        def lheight(node):
            if not node: return 0
            return lheight(node.left) + 1

        def rheight(node):
            if not node: return 0
            return rheight(node.right) + 1

        def count(node):
            if not node: return 0
            return count(node.left) + count(node.right) + 1

        l,r = lheight(root), rheight(root)

        if l > r: return count(root)
        else: return (2**l)-1

DFS()

Solution.analyze()
