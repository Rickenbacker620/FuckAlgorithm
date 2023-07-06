# https://leetcode.com/problems/path-sum-ii/

from utils import *

Solution.args(True, targetSum=22, root=tree_constructor([5,4,8,11,None,13,4,7,2,None,None,5,1]))

class DFS(Solution):
    def solve(self, root: TreeNode | None, targetSum):
        res_all = []
        res = []

        def dfs(node, sum):

            if not node:
                return

            if not node.left and not node.right and sum == node.val:
                res.append(node.val)
                res_all.append(res[:])
                res.pop()
                return

            res.append(node.val)
            dfs(node.left, sum-node.val)
            dfs(node.right, sum-node.val)
            res.pop()

        dfs(root, targetSum)
        return res_all

DFS()

class DFS2(Solution):
    def solve(self, root: TreeNode | None, targetSum):

        res_all = []
        res = [root.val]

        # NOTE compared to solution1 if we check in the begin of dfs, we dont need to
        # check for the first search point, otherwise, we need to special check
        # the first point we gonna seach
        # NOTE this also applies to the BFS method i wrote below
        # ANCHOR the two methods's difference lies in that
        # 1. the first one which check in the intial of dfs is like we step out first,
        # then we think if it is danger
        # 2. the second one is like, we stand in the current point and look for all possibles
        # if it is danger then we dont move to next
        # NOTE let us think that now, we are in dangerous place even at the starting point,
        # if we use the second strategy, we are ignore of the danger under out feet
        # but if we are the first strategy, we got the chance to check once
        # 😊 All in all, i think check every time is more reasonable and unified

        if not root:
            return res_all

        def dfs(node, sum):

            if not node.left and not node.right and sum == node.val:
                res_all.append(res[:])
                return

            sum_remain = sum - node.val

            if node.left:
                res.append(node.left)
                dfs(node.left, sum_remain)
                res.pop()

            if node.right:
                res.append(node.right)
                dfs(node.right, sum_remain)
                res.pop()

        dfs(root, targetSum)
        return res_all

DFS2()

class BFS(Solution):
    def solve(self, root: TreeNode | None, targetSum):

        res_all = []

        if not root:
            return res_all

        from collections import deque

        Q = deque()
        Q.append((root, targetSum, []))

        while Q:
            node, sum_remain, res = Q.popleft()

            if not node.left and not node.right and sum_remain == node.val:
                res_all.append(res[:] + [node.val])
                continue

            if node.left:
                Q.append((node.left, sum_remain-node.val, res[:]+[node.val]))

            if node.right:
                Q.append((node.right, sum_remain-node.val, res[:]+[node.val]))

        return res_all


BFS()


# this is simpler but loops more
class BFSSimplified(Solution):
    def solve(self, root: TreeNode | None, targetSum):

        res_all = []

        from collections import deque

        Q = deque([(root, targetSum, [])])

        while Q:
            node, sum_remain, res = Q.popleft()

            if not node: continue
            if not node.left and not node.right and sum_remain == node.val:
                res_all.append(res[:] + [node.val])
                continue


            Q.append((node.left, sum_remain-node.val, res[:]+[node.val]))
            Q.append((node.right, sum_remain-node.val, res[:] + [node.val]))

        return res_all



BFSSimplified()

Solution.analyze()
