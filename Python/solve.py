from functools import cache
from utils import *

Solution.args(3, coins=[1, 2, 5], amount=11)
Solution.args(2, coins=[1, 2], amount=3)
Solution.args(20, coins=[1, 2, 5], amount=100)
Solution.args(20, coins=[186, 419, 83, 408], amount=6249)


class SolutionWithCache(Solution):
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
        return res if res < float("inf") else -1


SolutionWithCache()


class SolutionPythonCache(Solution):
    def solve(self, coins, amount):
        coins.sort(reverse=True)

        if amount == 0:
            return 0

        @cache
        def dfs(amount):
            self._counter()
            if amount == 0: return 0

            return 1 + min([dfs(amount - coin) for coin in coins if amount >= coin] + [inf])


        res = dfs(amount)

        return res if res < float("inf") else -1


SolutionPythonCache()


class SolutionNoReturn(Solution):
    def solve(self, coins, amount):
        self.opt = inf
        self.ptr = 0

        coins.sort(reverse=True)

        if amount == 0:
            return 0

        def dfs(ptr, amount, cur):
            self._counter()
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
        return self.opt if self.opt < float("inf") else -1


SolutionNoReturn()

Solution.analyze()