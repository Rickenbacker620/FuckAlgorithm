from tabulate import tabulate
from colorama import Fore
from time import time
from pprint import pprint

class Arguments(list):

    def __call__(self, correct_answer=float("inf"), **kwargs):
        self.append({"ANS": correct_answer} | kwargs)


class Counter:
    count = 0

    def clear(self):
        self.count = 0

    def __call__(self):
        self.count += 1


class Solution:
    args = Arguments()
    _counter = Counter()
    _cache = Counter()
    _headers = ["TITLE", "MY", "TIME", "CO/CA"]
    _solutions = []

    @classmethod
    def analyze(cls):
        runs = [list(row) for row in zip(*cls._solutions)]
        for arg,run in zip(cls.args, runs):
            temparg = arg.copy()
            pprint(temparg, width=40)
            print(tabulate(run, cls._headers, "grid", ".5f"))

    def __init__(self):
        runs = []
        for idx, argset in enumerate(self.args):
            print(f"{self.__class__.__name__}--{idx}")
            tempargs = argset.copy()
            ans = tempargs.pop("ANS")
            start = time()
            myans = str(self.solve(**tempargs))
            ans_color = Fore.GREEN if myans == str(ans) else Fore.RED
            myans = ans_color + myans + Fore.RESET
            end = time()
            runs.append([self.__class__.__name__,
                myans,
                (end - start)*1e3,
                f"{self._counter.count}/{self._cache.count}"
            ])
            self._counter.clear()
            self._cache.clear()
        self.__class__._solutions.append(runs)

    def solve(self):
        pass

inf = float("inf")
