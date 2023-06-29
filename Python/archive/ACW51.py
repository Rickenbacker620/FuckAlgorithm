# https://www.acwing.com/problem/content/47/
from utils import *

Solution.args(nums=[1,2,3])
Solution.args(nums=[1,1,2])
Solution.args(nums=[1,1,1])
Solution.args(nums=[1,2,1])


class DFS(Solution):
    def solve(self, nums: list):
        used = [False] * len(nums)
        res = []
        res_all = []

        # NOTE this check is to force the dfs to grab the first orcurrence of the number as possible
        # since the number may be duplicate, we need to manually set an ordered rule for searching
        def check(idx):
            if used[idx]:
                return False

            first_i = nums.index(nums[idx])

            if idx == first_i:
                return True
            elif all([used[i] for i in range(first_i, idx) if nums[i] == nums[idx]]):
                return True
            else:
                return False



        def dfs(num_i):
            if num_i >= len(nums):
                res_all.append(res[:])
                return

            for i in range(len(nums)):
                if check(i):
                    res.append(nums[i])
                    used[i] = True
                    dfs(num_i+1)
                    used[i] = False
                    res.pop()

        dfs(0)
        return res_all

DFS()

class DFS2(Solution):
    def solve(self, nums: list):
        used = [False] * len(nums)
        res = []
        res_all = []

        def dfs(num_i):
            if num_i >= len(nums):
                res_all.append(res[:])
                return

            searched = []

            for i in range(len(nums)):
                if not used[i] and nums[i] not in searched:
                    searched.append(nums[i])
                    res.append(nums[i])
                    used[i] = True
                    dfs(num_i+1)
                    used[i] = False
                    res.pop()

        dfs(0)
        return res_all

DFS2()



Solution.analyze()
