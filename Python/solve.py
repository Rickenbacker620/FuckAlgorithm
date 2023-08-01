# https://leetcode.com/problems/invert-binary-tree/
from utils import *

class S(Solution):
    def solve(self, root):
        def invert(node):
            if not node: return

            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root

class S2(Solution):
    def solve(self, root):

        def invert(node):
            if not node:
                return node

            # temp = node.left
            # node.left = invert(node.right)
            # node.right = invert(temp)
            node.right, node.left = invert(node.left), invert(node.right)
            return node

        return invert(root)


Solution.analyze()
