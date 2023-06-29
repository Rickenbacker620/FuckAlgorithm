# https://www.acwing.com/problem/content/131/
from utils import *

Solution.args([str(i) for i in [123, 132, 213, 231, 321]], N=3)


class DFS(Solution):
    def solve(self, N):
        stack = []
        res = []
        res_all = []

        def dfs(train_i):
            if len(res) == N:
                res_all.append("".join(str(i) for i in res))
                return

            if stack:
                head = stack.pop()
                res.append(head)
                dfs(train_i)
                res.pop()
                stack.append(head)

            if train_i <= N:
                stack.append(train_i)
                dfs(train_i + 1)
                stack.pop()

        dfs(1)
        return res_all


DFS()

class DFSTrickOPT(Solution):
    def solve(self, N):
        stack = []
        res = []
        res_all = []

        def dfs(train_i):
            # NOTE if all trains are out, there can be one output order that is to pop all
            if train_i > N:
                res_tmp = res.copy()
                for train in stack[::-1]:
                    res_tmp.append(train)
                res_all.append("".join(str(i) for i in res_tmp))
                return

            if stack:
                head = stack.pop()
                res.append(head)
                dfs(train_i)
                res.pop()
                stack.append(head)

            stack.append(train_i)
            dfs(train_i + 1)
            stack.pop()

        dfs(1)
        return res_all

DFSTrickOPT()


class DFSSqueeze(Solution):
    def solve(self, N):
        res_all = []

        def dfs(train_i, cur, stack, res):
            if cur == N:
                res_all.append(str(res))
                return

            if stack:
                dfs(train_i, cur + 1, stack // 10, res * 10 + stack % 10)

            if train_i <= N:
                dfs(train_i + 1, cur, stack * 10 + train_i, res)

        dfs(1, 0, 0, 0)
        return res_all
# FIXME this cannot pass N >= 10 since it outputs 1234567890 instead of 12345678910

N = int(input())
s = DFSSqueeze()
res = s.solve(N)
output_lim = min(20, len(res))
for r in range(0, output_lim):
    print(res[r])


Solution.analyze()
