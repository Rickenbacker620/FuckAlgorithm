# https://leetcode.com/problems/number-of-islands/
from utils import *

Solution.args(
    1,
    grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ],
)

Solution.args(
    3,
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
)


class DFS(Solution):
    def solve(self, grid):

        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != "0"

        def walk(x, y):
            if not valid(x, y):
                return

            grid[x][y] = "0"

            for dx, dy in dirs:
                walk(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if valid(i,j):
                    res += 1
                    walk(i,j)

        return res

DFS()

class BFS(Solution):
    def solve(self, grid):

        from collections import deque
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        Q = deque()

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != "0"

        def walk(x, y):
            Q.append((x,y))

            while Q:
                x, y = Q.popleft()

                for dx, dy in dirs:
                    x_nxt, y_nxt = x+dx, y+dy
                    if valid(x_nxt,y_nxt):
                        grid[x_nxt][y_nxt] = "0"
                        Q.append((x_nxt, y_nxt))

        for i in range(m):
            for j in range(n):
                if valid(i,j):
                    res += 1
                    walk(i,j)

        return res

BFS()


Solution.analyze()
