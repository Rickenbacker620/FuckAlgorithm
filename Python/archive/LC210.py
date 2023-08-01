# https://leetcode.com/problems/course-schedule-ii/
from utils import *

# Solution.args([0,2,1,3], numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]])
Solution.args([0,1,2], numCourses=3, prerequisites=[[2,1],[1,0]])


class TopSort(Solution):
    def solve(self, numCourses: int, prerequisites:list[list[int]]):

        vlist = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for v1, v2 in prerequisites:
            vlist[v2].append(v1)
            indegrees[v1] += 1

        Q = [v for v in range(numCourses) if indegrees[v] == 0]
        ans = []
        count = 0

        while Q:
            cur = Q.pop(0)

            ans.append(cur)

            for nxt in vlist[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    Q.append(nxt)

        if len(ans) == numCourses:
            return ans
        else:
            return []



TopSort()

Solution.analyze()
