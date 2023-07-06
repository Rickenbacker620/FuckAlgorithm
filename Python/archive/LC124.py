# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from utils import *

Solution.args(6,root=tree_constructor([1,2,3]))
Solution.args(42, root=tree_constructor([-10,9,20,None,None,15,7]))
Solution.args(2, root=tree_constructor([2,-1,-2]))
Solution.args(12, root=tree_constructor([-1,None,9,-6,3,None,None,None,-2]))
Solution.args(-3, root=tree_constructor([-3]))


class BFS(Solution):
    def solve(self, root:TreeNode| None):
        self.opt = -inf

        def maxsum(node):
            if not node:
                return -inf

            ll = maxsum(node.left)
            rr = maxsum(node.right)
            self.opt = max(self.opt, ll, rr, ll+rr+node.val)
            return max(ll, rr, 0) + node.val

        return max(maxsum(root), self.opt)

BFS()

class BFS2(Solution):
    def solve(self, root:TreeNode| None):
        self.opt = -inf

        def maxsum(node):
            if not node:
                return -inf

            ll = maxsum(node.left)
            rr = maxsum(node.right)

            self.opt = max(self.opt, ll, rr, ll+rr+node.val)

            return max(ll, rr, 0) + node.val

        return max(maxsum(root), self.opt)

BFS2()

class BFS3(Solution):
    def solve(self, root:TreeNode| None):
        self.opt = -inf

        def maxsum(node):
            if not node:
                return 0

            ll = maxsum(node.left)
            rr = maxsum(node.right)
            ll = max(ll,0)
            rr = max(rr,0)

            self.opt = max(self.opt, ll+rr+node.val)

            return max(ll, rr) + node.val

        maxsum(root)
        return self.opt

BFS3()

Solution.analyze()