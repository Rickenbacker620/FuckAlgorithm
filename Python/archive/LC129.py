# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from utils import *

Solution.args(1026,root=tree_constructor([4,9,0, 5,1]))


class BFS(Solution):
    def solve(self, root:TreeNode| None):
        self.sum = 0

        def traverse(node, number):
            self._counter()
            if not node:
                return

            if not node.left and not node.right:
                self.sum += number*10+node.val
                return

            traverse(node.left, number*10+node.val)
            traverse(node.right, number*10+node.val)

        traverse(root, 0)
        return self.sum

BFS()

class BFSSimp(Solution):
    def solve(self, root:TreeNode| None):

        def traverse(node, number):
            self._counter()
            if not node:
                return 0

            number = number*10 + node.val

            if not node.left and not node.right:
                return number

            return traverse(node.right, number) + traverse(node.left, number)

        return traverse(root, 0)

BFSSimp()


Solution.analyze()