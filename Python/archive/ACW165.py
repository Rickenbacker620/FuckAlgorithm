# https://www.acwing.com/problem/content/description/167/
import sys
sys.path.append("/home/shiro/Projects/FuckAlgorithm/Python")
from utils import *

Solution.args(2, N=5, W=1996, cats=[1, 2, 1994, 12, 29])

# Solution.args(2, N=5, W=16, cats=[9, 5, 5, 5, 4, 3])

Solution.args(
    6,
    disabled=True,
    N=18,
    W=100000000,
    cats=[
        18381246,
        29249683,
        12495474,
        24844134,
        96242521,
        67846996,
        945213,
        27675252,
        58653213,
        12062801,
        4830609,
        83790642,
        10682393,
        27267295,
        60527976,
        8881456,
        3916444,
        32450339,
    ],
)

Solution.args(
    5,
    disabled=True,
    N=18,
    W=100000000,
    cats=[
        37597832,
        24520955,
        100000000,
        18509980,
        29141223,
        20287969,
        14028193,
        33097076,
        12116817,
        53439913,
        10216168,
        32891936,
        43952038,
        13463011,
        4056577,
        4646046,
        10153053,
        37881213,
    ],
)


class DFSBackTrack(Solution):
    def solve(self, N, W, cats):
        def dfs(weight):
            self._counter()

            if not cats:
                return 1

            children = []

            for cat in cats:
                cats.remove(cat)

                if weight >= cat:
                    children.append(dfs(weight - cat))
                else:
                    children.append(dfs(W - cat) + 1)

                cats.append(cat)

            return min(children)

        return dfs(W)


# DFSBackTrack() TLE



class DFSPassStateAsArgs(Solution):
    def solve(self, N, W, cats):
        def dfs(weight, catsrem):
            self._counter()

            if not catsrem:
                return 1

            children = []

            for cat in catsrem:
                cats_next = catsrem.copy()
                cats_next.remove(cat)

                if weight >= cat:
                    children.append(dfs(weight - cat, cats_next))
                else:
                    children.append(dfs(W - cat, cats_next) + 1)

            return min(children)

        return dfs(W, cats)


# DFSPassStateAsArgs() TLE

# FIXME Above two solutions are time out when the amount of cats are
# large, the DFS branches will increase drasticly, but in this problem
# cats are the only varing argument, so we need to use a smarter way to
# DFS. Compared with leetcode 322 change coins, the cat is the one and only
# element. Yet it cannot be cached since the duplicate function calls are less
# due to the unique cat and the uniq variance of weights of each cat, the solution
# or the parameter space of DFS is too sparse. Using dfs to find min child node is
# too dumb


# NOTE Lets think this problem as when choosing each cat, we can put it into the
# exist cars or lets make it a new car, then the branches closer to root will be less
# since when we put the first cat, and second cat, it only branches twice(second cat
# can only choose the first one or a new one, the third cat can only choose first or
# second or new one), also, when we iterate cats in decending order, we put the heaviest
# cat the first car, thus the first car has less space for others to choose, the best
# situation is say we have cars capacity 1000, first, second, third cats are
# 999, 998, 997, then we can almost be sure that these three cats cannot fall in the
# same car, the branches are must less, when i was using the wrong DFS, we still need
# to look forward to put cats weights smaller than the first cat every time

# NOTE Also why we can use DFS when only passing nth cat as argument is that
# the order of putting cat does not matter, so we can take it one at a time,
# search cat one by one, and the depth of the searching tree is always equal to
# number of cat, say we have 20 cats, the we need to search 20 levels
# This also the main difference from 322 change coin
# cause in that problem, we dont know how many level deep we need to find that answer
# so we need to have a return value of dfs like sum(dfs(...)+dfs(...)) or min(dfs(...), dfs(...))
# to get the report from deep level nodes
# in this case, we dont need to return thus we cannot use cache(we can use cache
# technically but this does not make significant improvement


class DFSCatByCat(Solution):
    def solve(self, N, W, cats):
        self.opt = inf

        cars = [[]]

        cats.sort(reverse=True)

        def check(cat, car):
            return W - sum(car) >= cat

        def dfs(cati):
            self._counter()
            print(cars)
            if len(cars) >= self.opt:
                return


            if cati == len(cats):
                self.opt = len(cars)
                return

            cat_w = cats[cati]

            for car in cars:
                if check(cat_w, car):
                    car.append(cat_w)
                    dfs(cati + 1)
                    car.pop()

            cars.append([cat_w])
            dfs(cati + 1)
            cars.pop()

        cars[0].append(cats[0])
        dfs(1)
        return self.opt


DFSCatByCat()

class DFSCarByCar(Solution):
    def solve(self, N, W, cats):
        self.opt = inf
        cars = [[]]
        used = [False] * N
        cats.sort(reverse=True)
        print(cats)

        def check(cat, car):
            return W - sum(car) >= cat

        def dfs(cati):
            self._counter()
            print(cars)
            if len(cars) >= self.opt:
                return

            if all(used):
                self.opt = len(cars)
                return

            flag = True

            for i in range(cati, N):
                cat_w = cats[i]
                if check(cat_w, cars[-1]) and not used[i]:
                    used[i] = True
                    cars[-1].append(cat_w)
                    dfs(cati + 1)
                    cars[-1].pop()
                    used[i] = False
                    flag = False
            if flag:
                cars.append([])
                dfs(0)
                cars.pop()

        dfs(0)
        return self.opt


DFSCarByCar()



class DFSOptimizedStateArg(Solution):
    def solve(self, N, W, cats):
        self.opt = inf

        cats.sort(reverse=True)

        def dfs(cati, cars):
            if len(cars) >= self.opt:
                return

            if cati == len(cats):
                self.opt = len(cars)
                return

            cat_w = cats[cati]

            for idx, car_w in enumerate(cars):
                if car_w >= cat_w:
                    cars_n = cars.copy()
                    cars_n[idx] -= cat_w
                    dfs(cati + 1, cars_n)

            cars_n = cars.copy()
            cars_n.append(W - cat_w)
            dfs(cati + 1, cars_n)

        dfs(0, [W])
        return self.opt


# DFSOptimizedStateArg()


# NOTE DP and next python flavor DP is enhanced from the first 2 DFS method
# the search branch tree is exactly the same
# However, it is still not good than the optimized DFS
# since the tree for the optimized one is cutted a lot
class DP(Solution):
    def solve(self, N, W, cats):
        dp = [inf] * (1 << N)
        remain = [0] * (1 << N)
        dp[0] = 0

        for statei in range(1, 1 << N):
            for cati in range(N):
                if bit_check(statei, cati):
                    statecur = bit_unset(statei, cati)
                    if dp[statecur] < dp[statei]:
                        if remain[statecur] >= cats[cati]:
                            dp[statei] = dp[statecur]
                            remain[statei] = remain[statecur] - cats[cati]
                        else:
                            dp[statei] = dp[statecur] + 1
                            remain[statei] = max(remain[statecur], W - cats[cati])

                    elif dp[statecur] == dp[statei] and remain[statecur] >= cats[cati]:
                        remain[statei] = max(
                            remain[statei], remain[statecur] - cats[cati]
                        )

        return dp[(1 << N) - 1]


# DP()


class DPPyFlavor(Solution):
    def solve(self, N, W, cats):
        class DPCell:
            def __init__(self):
                self.opt = inf
                self.rem = 0

        dp = [DPCell() for _ in range(1 << N)]
        dp[0].opt = 0

        # s_cur current dp state
        # s_pre possible previous dp state
        # c_i ith cat

        for s_cur in range(1, 1 << N):
            for c_i in range(N):
                if bit_check(s_cur, c_i):
                    s_pre = bit_unset(s_cur, c_i)

                    if dp[s_pre].opt < dp[s_cur].opt:  # we may found better answer
                        if dp[s_pre].rem >= cats[c_i]:  # if i can still put a cat
                            dp[s_cur].opt = dp[s_pre].opt
                            dp[s_cur].rem = dp[s_pre].rem - cats[c_i]

                        else:
                            dp[s_cur].opt = dp[s_pre].opt + 1  # if i cannot put cat
                            dp[s_cur].rem = max(dp[s_pre].rem, W - cats[c_i])

                    elif (
                        dp[s_pre].opt == dp[s_cur].opt and dp[s_pre].rem >= cats[c_i]
                    ):  # we already searched for it, no need to update, lets try to find a better remain value
                        dp[s_cur].rem = max(dp[s_cur].rem, dp[s_pre].rem - cats[c_i])

        return dp[(1 << N) - 1].opt

# ANCHOR
# This problem diff to Leetcode 322 coin change, why this cannot return value??
# No! it actually can, as long as we can represent the current state in the
# dfs arguments, that way we can even use cache to memorize
# but it is pretty hard though, we need to sqeeze the state
# also caching is does less work, since the states are merely overlap
# for example, in coin change, i can meet many times when i have a weigh of 11
# but in cat problem only we meet
# 1.cat remain [cat1, cat3, cat5]
# 2.cars remain [10,20,30]
# can we say that the problems are "overlapd", thus can be cached
# also the argument space is "sparse"
# so we need to possibly cut branches and find other methods to optimize

# DPPyFlavor()

Solution.analyze()
