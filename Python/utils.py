from typing import Any
from tabulate import tabulate
from colorama import Fore
from time import time
from pprint import pprint
from functools import cache
from math import inf
from copy import deepcopy


class Arguments(list):
    def __call__(self, correct_answer=None, disabled=False, **kwargs):
        if not disabled:
            self.append({"ANS": correct_answer} | kwargs)


class Counter:
    count = 0

    def clear(self):
        self.count = 0

    def __call__(self, explode=None):
        if explode and self.count == explode:
            exit(0)
        self.count += 1
        return self.count

class Timer:
    now = None
    locked = False
    def reset(self):
        self.locked = False
        self.now = None

    def __call__(self):
        if not self.locked:
            if self.now:
                print(f"Time {(time() - self.now)*1e3:.5f}ms")
                self.locked = True
            else:
                self.now = time()




class Solution:
    print_args = True
    args = Arguments()
    _counter = Counter()
    _cache = Counter()
    _timer = Timer()
    _headers = ["TITLE", "MY", "TIME", "CO/CA"]
    _solutions = []

    @classmethod
    def analyze(cls):
        runs = [list(row) for row in zip(*cls._solutions)]
        for arg, run in zip(cls.args, runs):
            temparg = arg.copy()
            if cls.print_args:
                print("\U0001F680" * 3)
                for k,v in temparg.items():
                    print(f"{k:<7}{v}")
                print()
            print(tabulate(run, cls._headers, "grid", ".5f"))

    def __init__(self):
        runs = []
        for idx, argset in enumerate(self.args):
            print(f"{self.__class__.__name__}--{idx}")
            tempargs = deepcopy(argset)
            ans = tempargs.pop("ANS")
            start = time()
            myans = str(self.solve(**tempargs))
            ans_color = Fore.GREEN if myans == str(ans) else Fore.RED
            myans = ans_color + myans + Fore.RESET
            end = time()
            runs.append(
                [
                    self.__class__.__name__,
                    myans,
                    (end - start) * 1e3,
                    f"{self._counter.count}/{self._cache.count}",
                ]
            )
            self._counter.clear()
            self._cache.clear()
            self._timer.reset()
        self.__class__._solutions.append(runs)

    def solve(self):
        pass


def bit_check(N, i):
    return True if N & (1 << i) else False

def bit_set(N, i):
    return N | (1 << i)

def bit_unset(N, i):
    return N & ~(1 << i)

class TreeNode:
    def __repr__(self) -> str:
        return str(self.val)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors:list[Node] = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return str(self.val)

def graph_constructor(nodes:list[list]):
    nodes_ = {i+1:Node(val=i+1) for i in range(len(nodes))}
    for i, neighbors in enumerate(nodes):
        for neigh in neighbors:
            nodes_[i+1].neighbors.append(nodes_[neigh])
    return nodes_[1]


def tree_constructor(nodes:list):
    nodes.reverse()

    if not nodes or not nodes[0]:
        return None

    root = TreeNode(nodes.pop())
    from collections import deque
    Q = deque()
    Q.append(root)

    while nodes:
        head = Q.popleft()
        l_nxt = nodes.pop()
        if l_nxt != None:
            head.left = TreeNode(l_nxt)
            Q.append(head.left)

        if not nodes:
            break

        r_nxt = nodes.pop()
        if r_nxt != None:
            head.right = TreeNode(r_nxt)
            Q.append(head.right)

    return root

def tree_preorder_traverse(node):
    if not node:
        return

    print(node)
    tree_preorder_traverse(node.left)
    tree_preorder_traverse(node.right)

def tree_inorder_traverse(node):
    if not node:
        return

    tree_inorder_traverse(node.left)
    print(node)
    tree_inorder_traverse(node.right)

def tree_postorder_traverse(node):
    if not node:
        return

    tree_postorder_traverse(node.left)
    tree_postorder_traverse(node.right)
    print(node)
