from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        i = 0
        j = len(letters)-1
        while i < j:
            k = int((i+j)/2)
            if letters[k] == target:
                if letters[k+1] == target:
                    i=k+1
                else:
                    return letters[k+1]
            elif letters[k] < target:
                if letters[k+1] > target:
                    return letters[k+1]
                else:
                    i=k+1
            else:
                j=k

print(Solution().nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))

