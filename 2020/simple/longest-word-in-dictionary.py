import math
from typing import List


class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = dict()
        self.is_word_end = False

    def add(self, child):
        self.children[child.val] = child


class Solution:
    def __init__(self):
        self.longest_words = set()
        self.longest = 0

    def longestWord(self, words: List[str]) -> str:
        root = Node('')
        for word in words:
            search = root
            for char in word:
                if char not in search.children:
                    search.add(Node(char))

                search = search.children[char]

            search.is_word_end = True

        # traversal the dictionary
        for child_key in root.children:
            self.traversal(root.children[child_key], '')

        if self.longest == 0:
            return ''

        self.longest_words = list(self.longest_words)
        self.longest_words.sort()
        return self.longest_words[0]

    def traversal(self, root: Node, curr_word):
        if root is None:
            return
        if not root.is_word_end:
            return

        curr_word += root.val

        if len(curr_word) > self.longest:
            self.longest_words.clear()
            self.longest_words.add(curr_word)
            self.longest = len(curr_word)
        elif len(curr_word) == self.longest:
            self.longest_words.add(curr_word)

        if len(root.children) > 0:  # 说明后面还有其他字母，且到本字母仍然是个单词
            for child_key in root.children:
                self.traversal(root.children[child_key], curr_word)


print(Solution().longestWord(
    words=["ogz", "eyj", "e", "ey", "hmn", "v", "hm", "ogznkb", "ogzn", "hmnm", "eyjuo", "vuq", "ogznk", "og", "eyjuoi",
           "d"]))
