# https://leetcode.com/problems/validate-binary-search-tree/
from utils import *


Solution.args(root=tree_constructor([5,4,6,None,None,3,7]))


class DFS(Solution):
    def solve(self, root: TreeNode | None):

        def validate(node: TreeNode | None):
            if not node:
                return True, None, None

            lvalid, lmax, lmin = validate(node.left)
            rvalid, rmax, rmin = validate(node.right)

            if not lvalid or not rvalid:
                return False, None, None
            if lmax != None and lmax >= node.val:
                return False, None, None
            if rmin != None and rmin <= node.val:
                return False, None, None

            return True, rmax or node.val, lmin or node.val

        v, _, _ = validate(root)
        return v

DFS()

class DFSOpt(Solution):
    def solve(self, root: TreeNode | None):

        def validate(node: TreeNode | None, left, right):
            if node is None:
                return True

            if node.val <= left or node.val >= right:
                return False

            return validate(node.left, left, node.val) and validate(node.right, node.val, right)

        return validate(root, float("-inf"), float("inf"))

DFSOpt()

# NOTE this uses the characteristic of BST, when we inorder traverse it, the numbers are visited by order
class DFSOpt2(Solution):
    def solve(self, root: TreeNode | None):
        inorder_list = []

        def inorder_traversal(node):
            if node == None:
                return
            inorder_traversal(node.left)
            inorder_list.append(node.val)
            inorder_traversal(node.right)
            return

        inorder_traversal(root)

        for i in range(1, len(inorder_list)):
            if inorder_list[i - 1] >= inorder_list[i]:
                return False

        return True

DFSOpt2()

Solution.analyze()