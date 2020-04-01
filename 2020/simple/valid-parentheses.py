class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or s == '':
            return True

        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif char == ')' and stack.pop() != '(':
                    return False

                elif char == ']' and stack.pop() != '[':
                    return False

                elif char == '}' and stack.pop() != '{':
                    return False

        return len(stack) == 0

print(Solution().isValid("([)]"))