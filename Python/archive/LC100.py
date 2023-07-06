# https://leetcode.com/problems/same-tree/
from utils import *

class S(Solution):
    def solve(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def traverse(p: TreeNode | None, q):

            if p == q == None:
                return True

            if p == None or q == None:
                return False

            if not traverse(p.left, q.left):
                return False

            if p == None or q == None or p.val != q.val:
                return False

            if not traverse(p.right, q.right):
                return False

            return True

        return traverse(p, q)


S()

# NOTE we dont need those |not|
class SOpt(Solution):
    def solve(self, p: TreeNode | None, q: TreeNode | None) -> None:

        def traverse(p: TreeNode | None, q):

            if p == q == None:
                return False

            if p == None or q == None:
                return True

            if traverse(p.left, q.left):
                return True

            if p == None or q == None or p.val != q.val:
                return True

            if traverse(p.right, q.right):
                return True

            return False

        traverse(p, q)

SOpt()

# more simplified
class SOpt2(Solution):
    def solve(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def traverse(p: TreeNode | None, q):

            if p == None or q == None:
                return p == q

            # NOTE using preorder traverse can cut the root faster
            return p.val == q.val and traverse(p.left, q.left) and traverse(p.right, q.right)

        return traverse(p, q)

SOpt2()


Solution.analyze()