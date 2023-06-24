# https://www.acwing.com/problem/content/1120/
from utils import *


Solution.print_args = False
Solution.args(3, N=6, nums=[14, 20, 33, 117, 143, 175])
Solution.args(3, N=6, nums=[149, 147, 49, 172, 19, 119])
Solution.args(2, N=4, nums=[3, 7, 6, 14])
Solution.args(2, N=10, nums=[3, 5, 7, 11, 13, 17, 19, 23, 46, 97])
Solution.args(5, N=10, nums = [185 ,182 ,363 ,363 ,489 ,17 ,85 ,429 ,228 ,59])
# N = int(input())
# nums = [int(i) for i in input().split()]
# s = Solution1()
# print(s.solve(N, nums))


class Brutal(Solution):
    def solve(self, N, nums):
        self.opt = inf

        grps = [[]]

        def check(num, grp):
            if grp == []:
                return True

            for b in grp:
                a = num
                while b:
                    a, b = b, a % b
                if a != 1:
                    return False

            return True

        def dfs(n_i):
            if n_i == N:
                self.opt = min(self.opt, len(grps))
                return

            num = nums[n_i]
            for grp in grps:
                if check(num, grp):
                    grp.append(num)
                    dfs(n_i + 1)
                    grp.remove(num)
            grps.append([num])
            dfs(n_i + 1)
            grps.pop()

        dfs(0)
        return self.opt


# Brutal()


class DFS(Solution):
    def solve(self, N, nums):
        self.opt = inf

        grps = [[]]

        def check(num, grp):
            if grp == []:
                return True

            for b in grp:
                a = num
                while b:
                    a, b = b, a % b
                if a != 1:
                    return False

            return True

        def dfs(n_i):
            self._counter()
            if len(grps) >= self.opt:
                return

            if n_i == N:
                self.opt = len(grps)
                return

            num = nums[n_i]
            for grp in grps:
                if check(num, grp):
                    grp.append(num)
                    dfs(n_i + 1)
                    grp.remove(num)
            grps.append([num])
            dfs(n_i + 1)
            grps.pop()

        dfs(0)
        return self.opt


DFS()


# FIXME: wrong answer in test case 3
# [3,7,6,14] ❌ [3,7], [6], [14]
# [3,7,6,14] ✔️ [6,7], [3, 14]


class IntuitiveSolutionButWA(Solution):
    def solve(self, N, nums: list):
        self.opt = inf

        def check(num, grp):
            from math import gcd

            return all(gcd(num, num_in_grp) == 1 for num_in_grp in grp)

        result = []

        for num in nums:
            found = False
            for sublist in result:
                if check(num, sublist):
                    sublist.append(num)
                    found = True
                    break
            if not found:
                result.append([num])
        return len(result)


# IntuitiveSolutionButWA()

class DFSV2(Solution):
    def solve(self, N, nums: list):
        self.opt = inf

        g = [[]]
        used = [False for _ in range(N)]


        def check(num, grp):
            from math import gcd
            return all(gcd(num, num_in_grp) == 1 for num_in_grp in grp)

        def dfs(start):
            self._counter()
            if len(g) >= self.opt: return

            if all(used):
                self.opt = len(g)
                return

            flag = True

            for i in range(start, N):
                if check(nums[i], g[-1]) and not used[i]:
                    used[i] = True
                    g[-1].append(nums[i])
                    dfs(i+1)
                    g[-1].pop()
                    used[i] = False
                    flag = False

            if flag:
                g.append([])
                dfs(0)
                g.pop()

        dfs(0)
        return self.opt

DFSV2()


Solution.analyze()
