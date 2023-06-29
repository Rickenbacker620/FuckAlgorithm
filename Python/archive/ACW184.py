# https://www.acwing.com/problem/content/186/
from utils import *

from string import ascii_uppercase

# Solution.args([1, 0, 3, 4, 2], N=5, arr=["ABCED", "BDACE", "EBBAA"])
Solution.args(
    [1, 0, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    disabled=False,
    N=21,
    arr=["BADCEFGHIJKLMNOPQRSTU", "BADCEFGHIJKLMNOPQRSTU", "BDEGIKMOQTBDEGIKMOQST"],
)

Solution.args(
    [1, 0, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    disabled=False,
    N=18,
    arr=
["FQAGNMBECLPOJDHIKR",
"ADQGABEHFDQADOKPML",
"LOCOLJFGIRMGJKQCDH"])

Solution.args(
    [4, 3, 9, 10, 1, 7, 11, 5, 8, 6, 2, 0],
    disabled=True,
    N=12,
    arr=["FDALHECBJKGI", "LIKAEDGJBCFH", "IJJAFLICDLFE"],
)


# FIXME TLE when data amount increase
class DFS(Solution):
    def solve(self, N, arr):
        res = []
        used = [False] * N
        self.res_out = []
        self.found = False

        # NOTE the validation part is the core part, while DFS is just the base one
        def validate():
            mapping = {ascii_uppercase[i]: res[i] for i in range(N)}
            carry = 0
            for digit in list(zip(*arr))[::-1]:
                a, b, c = [mapping[src] for src in digit]
                raw_sum = a + b + carry
                digit_sum, carry = raw_sum % N, raw_sum // N
                if digit_sum == c:
                    continue
                else:
                    return False
            return True

        def dfs(num_i):
            self._counter()
            if num_i >= N:
                if validate():
                    self.res_out = res[:]
                    self.found = True
                return

            for i in range(N):
                if not self.found and not used[i]:
                    used[i] = True
                    res.append(i)
                    dfs(num_i + 1)
                    res.pop()
                    used[i] = False

        dfs(0)


# DFS()


# FIXME TLE
class DFS2(Solution):
    def solve(self, N, arr):
        arr = [i for i in list(zip(*arr))[::-1]]

        mapping = {letter: -1 for letter in ascii_uppercase}

        digit_len = len(arr)

        self.found = False

        def dfs(digit_i, carry, used):
            temp = []
            for v in mapping.values():
                temp.append(v)

            if self.found:
                return

            if digit_i >= digit_len:
                for v in mapping.values():
                    if v != -1:
                        print(v, end=" ")
                print()
                self.found = True
                return

            a, b, c = arr[digit_i]
            an, bn, cn = [mapping[digit] for digit in arr[digit_i]]

            if min(an, bn) != -1:
                raw_sum = an + bn + carry
                carry_next = raw_sum // N
                tmp_c = raw_sum % N

                if cn == -1 and not bit_check(used, tmp_c):
                    mapping[c] = tmp_c
                    dfs(digit_i + 1, carry_next, used)
                    mapping[c] = -1
                elif cn != -1 and raw_sum % N == cn:
                    dfs(digit_i + 1, raw_sum // N, used)

            else:
                for digit in arr[digit_i]:
                    if mapping[digit] == -1:
                        for i in range(N):
                            if not bit_check(used, i):
                                mapping[digit] = i
                                dfs(digit_i, carry, bit_set(used, i))
                                mapping[digit] = -1

        dfs(0, 0, 0)


# DFS2()


class DFSOpt(Solution):
    def solve(self, N, arr):
        arr = [i for i in list(zip(*arr))[::-1]]

        used = [False] * N
        mapping = {letter: -1 for letter in ascii_uppercase}

        def check():
            carry = 0
            for idx, col in enumerate(arr):
                last_run = idx == len(arr) - 1
                a, b, c = [mapping[x] for x in col]
                if min(a, b, c) != -1:
                    if carry != -1:
                        raw_sum = a + b + carry
                        if raw_sum % N != c:
                            return False
                        if last_run and raw_sum >= N:
                            return False
                        carry = raw_sum // N
                    else:
                        if (a + b) % N != c and (a + b + 1) % N != c:
                            return False
                        if last_run and a + b >= N:
                            return False
                else:
                    carry = -1

            return True

        def dfs(letter_i):
            self._counter()
            if letter_i == N:
                output_str = " ".join(str(x) for x in mapping.values() if x != -1)
                print(output_str)
                return True

            for i in range(N):
                if not used[i]:
                    used[i] = True
                    mapping[ascii_uppercase[letter_i]] = i
                    if check() and dfs(letter_i + 1):
                        return True
                    mapping[ascii_uppercase[letter_i]] = -1
                    used[i] = False
            return False

        dfs(0)


# DFSOpt()


class DFSOpt2(Solution):
    def solve(self, N, arr):
        arr = [i for i in list(zip(*arr))[::-1]]

        arr = [[ascii_uppercase.index(i) for i in tup] for tup in arr]
        # arr = [(ascii_uppercase.index(x) for x in i) for i in list(zip(*arr))[::-1]]

        res = [-1] * N

        used = [False] * N

        def check():
            carry = None

            for i in range(N - 1, 0, -1):
                a, b, c = [res[x] for x in arr[i]]

                if min(a, b, c) != -1:
                    if carry != -1:
                        raw_sum = a + b + carry
                        if raw_sum % N != c:
                            return False
                        if not i and raw_sum >= N:
                            return False
                        carry = raw_sum // N
                    else:
                        if (a + b) % N != c and (a + b + 1) % N != c:
                            return False
                        if not i and a + b >= N:
                            return False
                else:
                    carry = None

            return True

        def dfs(letter_i):
            self._counter()
            if letter_i == N:
                print(res)
                return True

            for i in range(N):
                if not used[i]:
                    used[i] = True
                    res[letter_i] = i
                    if check() and dfs(letter_i + 1):
                        return True
                    res[letter_i] = -1
                    used[i] = False
            return False

        dfs(0)


# DFSOpt2() TLE

# NOTE OPT1 and OPT2 are not actually optimized
# to optimize this ,we need to make sure the lower bits are filled as soon as possible

class DFSOptFin(Solution):
    def solve(self, N, arr):
        arr = [i for i in list(zip(*arr))[::-1]]

        arr = [[ascii_uppercase.index(i) for i in tup] for tup in arr]

        next = []
        for tup in arr:
            for i in tup:
                if i not in next:
                    next.append(i)

        res = [None] * N

        used = [False] * N

        def check():
            carry = 0

            for i in range(N):
                a, b, c = [res[x] for x in arr[i]]

                # if None not in (a,b,c): # if all nums in that col is filled
                if a != None and b != None and c != None:
                    if carry != None:
                        raw_sum = a + b + carry
                        if raw_sum % N != c:
                            return False
                        if i == N-1 and raw_sum >= N:
                            return False
                        carry = raw_sum // N
                    else:
                        if (a + b) % N != c and (a + b + 1) % N != c:
                            return False
                        if i == N-1 and a + b >= N:
                            return False
                else:
                    carry = None

            return True

        def dfs(letter_i):
            self._counter()
            if letter_i == N:
                print(" ".join(str(x) for x in res))
                return True

            for i in range(N):
                if not used[i]:
                    used[i] = True
                    res[next[letter_i]] = i
                    if check() and dfs(letter_i + 1):
                        return True
                    res[next[letter_i]] = None
                    used[i] = False
            return False

        dfs(0)

# DFSOptFin() # NOTE AC Verion but still TLE since py code slow, switch to C++ can AC✅

class DFSOptFinV2(Solution):
    def solve(self, N, arr):

        arr = [i for i in list(zip(*arr))[::-1]]
        arr = [[ascii_uppercase.index(i) for i in tup] for tup in arr]

        next = []
        for tup in arr:
            for i in tup:
                if i not in next:
                    next.append(i)

        # NOTE using None is simple and easy to read, but it is slower
        res = [-1] * N

        used = [False] * N

        def check():
            carry = 0

            for i in range(N):

                col = arr[i]
                a, b, c = res[col[0]], res[col[1]], res[col[2]]

                # if None not in (a,b,c): # if all nums in that col is filled
                if a != -1 and b != -1 and c != -1:
                    if carry != -1:
                        raw_sum = a + b + carry
                        if raw_sum % N != c:
                            return False
                        if i == N-1 and raw_sum >= N:
                            return False
                        carry = raw_sum // N

                    else:
                        if (a + b) % N != c and (a + b + 1) % N != c:
                            return False
                        if i == N-1 and a + b >= N:
                            return False
                else:
                    carry = -1

            return True

        def dfs(letter_i):
            # self._counter()
            if letter_i == N:
                print(" ".join(str(x) for x in res))
                return True

            for i in range(N):
                if not used[i]:
                    used[i] = True
                    res[next[letter_i]] = i
                    if check() and dfs(letter_i + 1):
                        return True
                    res[next[letter_i]] = -1
                    used[i] = False
            return False

        dfs(0)

DFSOptFinV2() # NOTE AC Verion but still TLE since py code slow, switch to C++ can AC✅

# N = int(input())
# arr = [input() for _ in range(3)]

# s = DFSOpt()
# s.solve(N, arr)


Solution.analyze()
