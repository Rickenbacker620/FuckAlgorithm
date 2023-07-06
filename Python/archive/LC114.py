# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from utils import *

Solution.args(root=tree_constructor([1,2,5,3,4,None,6]))


class DFS(Solution):
    def solve(self, root):
        self.pre = None

        def traverse(node):
            if not node:
                return

            ll = node.left
            rr = node.right

            if self.pre:
                self.pre.right = node
                self.pre.left = None

            self.pre = node

            traverse(ll)
            traverse(rr)

        traverse(root)


DFS()

Solution.analyze()