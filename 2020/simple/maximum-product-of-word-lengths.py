from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        max_product = 0
        for i in range(n):
            word = words[i]
            char_set = set(word)
            for j in range(i + 1, n):
                word2 = words[j]
                join = False
                word2_set = set(word2)
                for char in word2_set:
                    if char in char_set:
                        join = True
                        break

                if join is False:
                    result = len(word) * len(word2)
                    if result > max_product:
                        max_product = result

        return max_product


print(Solution().maxProduct(["a","aa","aaa","aaaa"]))
