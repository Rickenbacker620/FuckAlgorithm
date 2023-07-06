# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from utils import *

Solution.args(root=tree_constructor([1,2,3,4,5,6,7]))

class BFS(Solution):
    def solve(self, root:TreeNode| None):
        if not root:
            return None
        from collections import deque

        Q1 = deque()
        Q2 = deque()
        Q1.append(root)

        while Q1:
            while Q1:
                head = Q1.popleft()
                if head.left:
                    Q2.append(head.left)
                if head.right:
                    Q2.append(head.right)

            for i in range(len(Q2)-1):
                Q2[i].next = Q2[i+1]

            Q1, Q2 = Q2, Q1

        return root

BFS()

class BFSOpt(Solution):
    def solve(self, root:TreeNode| None):
        from collections import deque
        Q = deque()

        if not root:
            return root

        Q.append(root)

        while Q:
            qlen = len(Q)

            prev = None
            for _ in range(qlen):
                node = Q.popleft()
                node.next = prev
                prev = node

                if node.right:
                    Q.append(node.right)

                if node.left:
                    Q.append(node.left)

        return root

BFSOpt()

Solution.analyze()