from typing import List


class Solution:
    def __init__(self):
        self.lines = [{'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'},
                      {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'},
                      {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}]
        self.line_count = 3

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            line_index = -1
            is_same_line = True
            for char in word.upper():
                if line_index >= 0:
                    if char not in self.lines[line_index]:
                        is_same_line = False
                        break
                else:
                    for i in range(self.line_count):
                        if char in self.lines[i]:
                            line_index = i
                            break

            if is_same_line:
                result.append(word)

        return result


print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
