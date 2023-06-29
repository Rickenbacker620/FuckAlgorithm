# NOTE this is not finished
# https://www.acwing.com/problem/content/description/187/
from utils import *

Solution.args(steps=3, board=[[1,0], [2,1,0], [2,3,4,0], [3,1,0], [2,4,3,4,0]])
Solution.args(steps=2, board=[[1,0],[1,0],[0],[1,0],[1,0]])

# Solution.args(steps=5, board= [[1, 1, 2, 3, 4, 0], [3, 3, 1, 2, 3, 5, 4, 0], [3, 5, 5, 3, 2, 2, 0], [5, 5, 3, 5, 2, 4, 2], [0, 0, 0, 0, 0, 0, 0]])

class Primitive(Solution):
    def solve(self, steps, board):

        H = max(len(col) for col in board) - 1
        W = 5
        res = []
        total = H*W
        num_cnt = {}


        def pb(board):
            for j in range(H-1, -1 , -1):
                for i in range(W):
                    print(board[i][j], end="")
                print()
            print("------")

        for col in board:
            col.pop()
            while len(col) != H:
                col.append(0)
                total -= 1

        def fall(board):
            for col in board:
                idx = 0
                for e in col:
                    if e != 0:
                        col[idx] = e
                        idx += 1


                for i in range(idx, len(col)):
                    col[i] = 0

        def check(board, i, j):
            tmp_arr = []
            for col in board:
                for e in col:
                    if e != 0:
                        tmp_arr.append(e)

            from collections import Counter
            c = Counter(tmp_arr)
            for cn in c.values():
                if cn < 5:
                    return False

            return board[i][j] or board[i+1][j]

        def scan(board, dim1, dim2):
            marked_pts = set()
            for i in range(dim1):
                pts = []
                count = 0
                num = None

                for j in range(dim2):
                    if dim1 == H:
                        i_, j_ = j, i
                    else:
                        i_, j_ = i, j
                    e = board[i_][j_]

                    if e != num:
                        if count >= 3:
                            for pt in pts:
                                marked_pts.add(pt)

                        if e == 0:
                            num = None
                            pts.clear()
                            count = 0
                            continue

                        num = e
                        pts.clear()
                        pts.append((i_,j_))
                        count = 1

                    else:
                        pts.append((i_,j_))
                        count += 1

                if len(pts) >= 3:
                    for pt in pts:
                        marked_pts.add(pt)


            return marked_pts

        def settle(board):

            canceled = 0

            fall(board)

            while True:

                mk1 = scan(board, H, W)
                mk2 = scan(board, W, H)

                mkall = mk1 | mk2


                if not mkall:
                    break

                for pt in mkall:
                    board[pt[0]][pt[1]] = 0
                    canceled += 1

                fall(board)


            return canceled




        def dfs(board, step, blk_rem):
            self._counter()
            if blk_rem == 0:
                for i,j,d in res:
                    print(i,j,d)
                return True

            if step == 0:
                return

            from itertools import product
            from copy import deepcopy

            for i, j in product(range(W-1), range(H)):
                if check(board, i, j):
                    board_= deepcopy(board)

                    dir = 1 if board_[i][j] else -1
                    board_[i][j], board_[i+1][j] = board_[i+1][j], board_[i][j]

                    res.append((i, j, dir))
                    blks = settle(board_)
                    if dfs(board_, step-1, blk_rem-blks):
                        return True
                    res.pop()
            return False

        # dfs(board, steps, total)
        if not dfs(board, steps, total):
            print("-1")

Primitive()

# step = int(input())
# arr = [[int(i) for i in input().split()] for _ in range(5)]
# s = Primitive()
# s.solve(steps=step, board=arr)

Solution.analyze()