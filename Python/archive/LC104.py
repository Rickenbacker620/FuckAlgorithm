# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from utils import *

class S(Solution):
    def solve(self, root: TreeNode | None) -> int:

        def maxdep(node: TreeNode | None):
            if not node: return 0

            return max(maxdep(node.left), maxdep(node.right)) + 1

        return maxdep(root)


Solution.analyze()