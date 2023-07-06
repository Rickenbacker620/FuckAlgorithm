# https://leetcode.com/problems/balanced-binary-tree/
from utils import *

Solution.args(root=tree_constructor([1, 2, 2, 3, None, None, 3, 4, None, None, 4]))


class S(Solution):
    def solve(self, root: TreeNode | None) -> int:
        if not root:
            return True

        def dep(node: TreeNode | None):
            if not node:
                return True, 0

            lflag, ldep = dep(node.left)
            rflag, rdep = dep(node.right)

            flag = lflag and rflag and abs(ldep - rdep) <= 1
            mdep = max(ldep, rdep) + 1

            return flag, mdep

        flag, _ = dep(root)
        return flag

S()

# NOTE merge the depth of node which cannot be searched to -1
class SqueezeStatus(Solution):
    def solve(self, root: TreeNode | None) -> int:
        if not root:
            return True

        def dep(node: TreeNode | None):
            if not node:
                return 0

            ldep = dep(node.left)
            rdep = dep(node.right)

            if ldep < 0 or rdep < 0 or abs(ldep - rdep) > 1:
                return -1
            else:
                return max(ldep, rdep) + 1

        return dep(root) >= 0

SqueezeStatus()

Solution.analyze()
