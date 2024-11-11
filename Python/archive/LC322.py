# https://leetcode.com/problems/coin-change/
from utils import *

Solution.args(3, coins=[1, 2, 5], amount=11)
Solution.args(2, coins=[1, 2], amount=3)
Solution.args(1, coins=[1, 2], amount=2)
Solution.args(20, coins=[1, 2, 5], amount=100)
Solution.args(20, coins=[186, 419, 83, 408], amount=6249)
Solution.args(2, coins=[1, 2147483647], amount=2)
# DFS cut branch failed on this test case
# since the every possible step (in this case is coin value) are close to each other
# however, branch cut is based on greedy algorithm, so we cannot cut too much branches
# In general, when the step is close to each other, DFS is not a good choice
# However, this problem can be solved using DP or memoization
# why memorization? because the solution space is dense, we have a lot of repeated subproblems
Solution.args(1, coins=[411,412,413,414,415,416,417,418,419,420,421,422], amount=9864)


class SolutionDFSCustomCache(Solution):
    def solve(self, coins, amount):
        cache = {}

        coins.sort(reverse=True)

        if amount == 0:
            return 0

        def dfs(amount):
            if amount in cache:
                return cache[amount]
            self._counter()

            if amount == 0:
                return 0

            braches = [dfs(amount - coin) for coin in coins if amount >= coin]
            cache[amount] = 1 + min(braches) if braches else inf

            return cache[amount]

        res = dfs(amount)
        return res if res < inf else -1


SolutionDFSCustomCache()


class SolutionDFSPythonCache(Solution):
    def solve(self, coins, amount):
        coins.sort(reverse=True)

        if amount == 0:
            return 0

        @cache
        def dfs(amount):
            self._counter()
            if amount == 0:
                return 0

            return 1 + min(
                [dfs(amount - coin) for coin in coins if amount >= coin] + [inf]
            )

        res = dfs(amount)

        return res if res < inf else -1


SolutionDFSPythonCache()


class SolutionDFSCutBranches(Solution):
    def solve(self, coins, amount):
        self.opt = inf
        self.ptr = 0

        coins.sort(reverse=True)

        if amount == 0:
            return 0

        def dfs(ptr, amount, cur):
            if amount == 0:
                self.opt = cur
                return

            for i in range(ptr, len(coins)):
                coin = coins[i]
                if amount >= coin and (self.opt - cur) * coin > amount:
                    dfs(i, amount - coin, cur + 1)

            return

        for i in range(len(coins)):
            dfs(i, amount, 0)
        return self.opt if self.opt < inf else -1


SolutionDFSCutBranches()


class SolutionDPDict(Solution):
    def solve(self, coins, amount):
        state = {0: 0} | {coin: 1 for coin in coins}

        start = min(coins)

        for w in range(start, amount + 1):
            if w in state:
                continue

            candidates = [state[w - coin] for coin in coins if w - coin in state]

            if candidates:
                state[w] = 1 + min(candidates)

        return state.get(amount, -1)


SolutionDPDict()


class SolutionDPList(Solution):
    def solve(self, coins, amount):
        dp = [0] + [inf] * amount

        for i in range(1, amount + 1):
            dp[i] = 1 + min([dp[i - c] for c in coins if i >= c] or [inf])
        return dp[-1] if dp[-1] < inf else -1


SolutionDPList()


class SolutionBFS(Solution):
    def solve(self, coins, amount):
        self.opt = inf
        q = []
        coins.sort(reverse=True)

        q.append((amount, 0, inf))
        while q:
            self._counter()
            node = q.pop(0)
            for coin in coins:
                remain, cur, last_coin = node
                if remain == 0:
                    return cur
                if remain >= coin and coin <= last_coin:
                    q.append((remain-coin, cur+1, coin))
        return self.opt


SolutionBFS()

Solution.analyze()
