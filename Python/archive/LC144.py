# https://leetcode.com/problems/binary-tree-preorder-traversal/
from utils import *

class DFS(Solution):
    def solve(self, root):
        nodes = []

        def traverse(node):
            if not node:
                return

            nodes.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return nodes

Solution.analyze()