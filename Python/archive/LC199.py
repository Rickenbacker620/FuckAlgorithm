# https://leetcode.com/problems/binary-tree-right-side-view/
from utils import *

# Solution.args(root=tree_constructor([1,2,3,None,5,None,4]))
Solution.args(root=tree_constructor([1,2,3,4]))
# Solution.args(root=tree_constructor([1,2]))

class DFS(Solution):
    def solve(self, root):

        nodes = []
        def dfs(node, maxlen):
            if not node:
                return

            if len(nodes) <= maxlen:
                nodes.append(node.val)

            dfs(node.right, maxlen+1)
            dfs(node.left, maxlen+1)

        dfs(root, 0)
        return nodes

DFS()

class BFS(Solution):
    def solve(self, root):
        if root is None:
            return None
        from collections import deque
        Q = deque([root])
        Q_ = deque()
        nodes = []

        while Q:
            nodes.append(Q[0].val)
            while Q:
                cur = Q.popleft()
                if cur.right:
                    Q_.append(cur.right)
                if cur.left:
                    Q_.append(cur.left)

            Q, Q_ = Q_, Q
        return nodes

BFS()

Solution.analyze()
