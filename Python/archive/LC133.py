# https://leetcode.com/problems/clone-graph/
from utils import *

Solution.args(node=graph_constructor([[2,4],[1,3],[2,4],[1,3]]))

class DFS(Solution):


    def solve(self, node:Node):
        if not node:
            return None

        cloned = {}

        def dclone(node:Node):
            cloned[node] = node_ = Node(node.val)
            for nei in node.neighbors:
                if nei not in cloned:
                    cloned[nei] = dclone(nei)
                node_.neighbors.append(cloned[nei])
            return node_

        return dclone(node)


DFS()

#simpler
class DFS2(Solution):

    def solve(self, node:Node):
        cloned = {None:None}

        def dclone(node:Node):
            if node in cloned: return cloned[node]
            cloned[node] = Node(node.val)
            cloned[node].neighbors = [dclone(neighbor) for neighbor in node.neighbors]
            return node_

        return dclone(node)

DFS2()

# BFS Flavor
class BFS(Solution):

    def solve(self, node:Node):
        from collections import deque

        if not node: return None

        Q = deque([node])
        cloned = {node: Node(node.val)}

        while Q:
            cur = Q.popleft()
            cur_ = cloned[cur]

            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    Q.append(neighbor)
                cur_.neighbors.append(cloned[neighbor])

        return cloned[node]

BFS()

class BFS2(Solution):

    def solve(self, node:Node):
        if not node:
            return None

        from collections import deque

        Q = deque([node])
        cloned = {node: Node(node.val)}

        while Q:
            cur = Q.popleft()
            cur_ = cloned[cur]

            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    Q.append(neighbor)
                cur_.neighbors.append(cloned[neighbor])

        return cloned[node]

BFS2()

Solution.analyze()