# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class WordDictionary:

    def __init__(self):
        self.tree = Node(None)

    def addWord(self, word: str) -> None:
        word = word + ";"
        cur = self.tree

        for letter in word:
            found = False
            for child in cur.children:
                if child.val == letter:
                    cur = child
                    found = True
                    break

            if not found:
                next = Node(letter)
                cur.children.append(next)
                cur = next



    def search(self, word: str) -> bool:
        word = word + ";"
        word_length = len(word)


        def dfs(letter_i, node):
            if letter_i >= word_length:
                return True

            letter = word[letter_i]
            for child in node.children:
                if letter == '.' or child.val == letter:
                    if dfs(letter_i+1, child):
                        return True

            return False

        res = dfs(0, self.tree)
        print(res)
        return res



class WordDictionaryOptDFS:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        word = word + ";"
        cur = self.tree

        for letter in word:
            cur = cur.setdefault(letter, {})


    def search(self, word: str) -> bool:
        word = word + ";"
        word_length = len(word)


        def dfs(letter_i, node):
            if letter_i >= word_length:
                return True

            letter = word[letter_i]

            for letter_, children_ in node.items():
                if (letter == letter_ or letter == '.') and dfs(letter_i+1, children_):
                    return True

            return False

        return dfs(0, self.tree)

class WordDictionaryOptBFS:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        word = word + ";"
        cur = self.tree

        for letter in word:
            cur = cur.setdefault(letter, {})


    def search(self, word: str) -> bool:
        word = word + ";"

        Q = [self.tree]
        Q_ = []

        for letter in word:

            while Q:
                cur = Q.pop(0)

                for letter_, children_ in cur.items():
                    if letter_ == ";" == letter:
                        return True

                    if letter == letter_ or letter == '.':
                        Q_.append(children_)

            Q, Q_ = Q_, Q

        return False


wordDictionary = WordDictionaryOptBFS()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
# wordDictionary.search(".")
# wordDictionary.search("a")
# wordDictionary.search("aa")
# wordDictionary.search("a")
# wordDictionary.search(".a")
wordDictionary.search("a.")
wordDictionary.search("a")
wordDictionary.search("b")



wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad") # False
wordDictionary.search("bad") # True
wordDictionary.search(".ad") # True
wordDictionary.search("b..") # True
