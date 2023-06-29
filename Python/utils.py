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

def tree_constructor(node_list: list[int|None]) -> TreeNode:

    root = TreeNode(node_list[0])
    curr = [root]
    ptr = 1

    while ptr < len(node_list):
        curr2 = []
        for c in curr:

            if node_list[ptr] is not None:
                new = TreeNode(node_list[ptr])
                c.left = new
                curr2.append(new)
            ptr += 1

            if ptr >= len(node_list):
                break

            if node_list[ptr] is not None:
                new = TreeNode(node_list[ptr])
                c.right = new
                curr2.append(new)
            ptr += 1
        curr = curr2
    return root