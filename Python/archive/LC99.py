# https://leetcode.com/problems/recover-binary-search-tree/
from utils import *

# Solution.args(root=tree_constructor([3,1,4,None,None,2]))
Solution.args(root=tree_constructor([1,3,None,None,2]))

# NOTE we need to find two abnormal ordered pairs
class S(Solution):
    def solve(self, root: TreeNode | None) -> None:
        brokens = []
        self.pre = None

        def traverse(node: TreeNode | None):

            if len(brokens) == 2:
                return

            if not node:
                return

            traverse(node.left)

            if self.pre and node.val < self.pre.val:
                brokens.append((self.pre, node))

            self.pre = node

            traverse(node.right)

        traverse(root)

        brokens[0][0].val, brokens[-1][1].val = brokens[-1][1].val, brokens[0][0].val

S()

Solution.analyze()