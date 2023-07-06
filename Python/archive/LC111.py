# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from utils import *

Solution.args(root=tree_constructor([2,None,3,None,4,None,5,None,6]))

class DFS(Solution):
    def solve(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dep(node: TreeNode | None):
            self._counter()
            if not node: return inf

            if not node.left and not node.right: return 1

            return min(dep(node.left), dep(node.right)) + 1

        return dep(root)

DFS()

# this is faster since we can directly cut the branch if they are not exist, not entering the dep() for empty left or empty right

class DFS2(Solution):
    def solve(self, root: TreeNode | None) -> int:

        def dep(node: TreeNode | None):
            self._counter()
            if not node: return 0

            if not node.left and not node.right: return 1

            if not node.left:
                return 1 + dep(node.right)

            if not node.right:
                return 1 + dep(node.left)

            return min(dep(node.left), dep(node.right)) + 1

        return dep(root)

DFS2()

# DFS since we can stop after find the minimum one
class BFS(Solution):
    def solve(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        self.cnt = 0

        from collections import deque
        Q = deque()
        Q.append((root, 1))

        while Q:
            node, level = Q.popleft()

            if not node.left and not node.right:
                self.cnt = level
                break

            if node.left:
                Q.append((node.left, level + 1))
                self.cnt = level+1

            if node.right:
                Q.append((node.right, level + 1))
                self.cnt = level+1

        return self.cnt

BFS()

Solution.analyze()