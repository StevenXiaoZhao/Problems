from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        result = []
        for char in seq:
            count = len(stack)
            if char == '(':
                num = 0 if count == 0 or stack[count - 1] == 1 else 1
                stack.append(num)
                result.append(num)
            else:
                result.append(stack.pop())
                str= ''
                str.isnumeric()
                

        return result
