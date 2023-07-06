# https://leetcode.com/problems/symmetric-tree/
from utils import *

class S(Solution):
    def solve(self, root: TreeNode | None) -> bool:

        def check(p, q):
            if p == None or q == None: return p == q

            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)

Solution.analyze()