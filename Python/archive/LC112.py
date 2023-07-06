# https://leetcode.com/problems/path-sum/
from utils import *

Solution.args(True, targetSum=22, root=tree_constructor([5,4,8,11,None,13,4,7,2,None,None,None,1]))

Solution.args(False, targetSum=2, root=tree_constructor([1,2]))

Solution.args(False,targetSum=0, root=[])
class DFS(Solution):
    def solve(self, root: TreeNode | None, targetSum) -> bool:

        def dfs(node, sum):
            if not node:
                return False

            if not node.left and not node.right and sum == node.val:
                return True

            return dfs(node.left, sum-node.val) or dfs(node.right, sum-node.val)

        return dfs(root, targetSum)

DFS()

class BFS(Solution):
    def solve(self, root: TreeNode | None, targetSum) -> bool:
        if not root:
            return False

        from collections import deque

        Q = deque()
        Q.append((root, targetSum))

        while Q:
            node, sum_remain = Q.popleft()

            if not node.left and not node.right and sum_remain == node.val:
                return True

            if node.left:
                Q.append((node.left, sum_remain-node.val))

            if node.right:
                Q.append((node.right, sum_remain-node.val))

        return False


BFS()


# this is simpler but loops more
class BFSSimplified(Solution):
    def solve(self, root: TreeNode | None, targetSum) -> bool:

        from collections import deque

        Q = deque([(root, targetSum)])

        while Q:
            node, sum_remain = Q.popleft()

            if not node: continue
            if not node.left and not node.right and sum_remain == node.val: return True

            Q.append((node.left, sum_remain-node.val))
            Q.append((node.right, sum_remain-node.val))

        return False


BFSSimplified()

Solution.analyze()
