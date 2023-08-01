# https://leetcode.com/problems/binary-tree-postorder-traversal/
from utils import *

class DFS(Solution):
    def solve(self, root):
        nodes = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            traverse(node.right)
            nodes.append(node.val)

        traverse(root)
        return nodes


Solution.analyze()
