# https://leetcode.com/problems/surrounded-regions/
from utils import *

Solution.args(board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
Solution.args(board=[["O","O"],["O","O"]])
Solution.args(board=[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])
Solution.args(board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])


class DFS(Solution):
    def solve(self, board):
        M = len(board)
        N = len(board[0])

        dirs = [[-1,0],[1,0], [0,-1],[0,1]]

        def check(i, j):
            return 0 <= i < M and 0 <= j < N and board[i][j] != 'X' and board[i][j] != 'o'

        def dfs(i, j):
            if board[i][j] == 'X':
                return

            board[i][j] = 'o'

            for dir in dirs:
                i_nxt, j_nxt = i+dir[0], j+dir[1]
                if check(i_nxt, j_nxt):
                    dfs(i_nxt, j_nxt)

        for i in range(1, M-1):
            dfs(i, 0)
            dfs(i, N-1)

        for j in range(N):
            dfs(0,j)
            dfs(M-1, j)

        for i, row in enumerate(board):
            for j, e in enumerate(row):
                if e == 'o':
                    board[i][j] = 'O'
                if e == 'O':
                    board[i][j] = 'X'


DFS()

class BFS(Solution):
    def solve(self, board):
        M = len(board)
        N = len(board[0])

        dirs = [[-1,0],[1,0], [0,-1],[0,1]]

        def check(i, j):
            return 0 <= i < M and 0 <= j < N and board[i][j] != 'X' and board[i][j] != 'o'

        from collections import deque
        Q = deque()

        for i in range(1, M-1):
            Q.append((i, 0))
            Q.append((i, N-1))

        for j in range(N):
            Q.append((0,j))
            Q.append((M-1, j))

        while Q:
            i, j = Q.popleft()

            if not check(i, j):
                continue

            board[i][j] = 'o'

            for dir in dirs:
                i_nxt, j_nxt = i+dir[0], j+dir[1]
                Q.append((i_nxt, j_nxt))

        for i, row in enumerate(board):
            for j, e in enumerate(row):
                if e == 'o':
                    board[i][j] = 'O'
                if e == 'O':
                    board[i][j] = 'X'


BFS()

Solution.analyze()