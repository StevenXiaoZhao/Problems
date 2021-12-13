class Solution:
    def myAtoi(self, str: str) -> int:
        num = 0
        negative = False
        num_start = False
        max_val = int(pow(2, 31))
        for char in str:
            if num_start is False:
                if char == ' ':
                    continue
                elif char == '+':
                    num_start = True
                elif char == '-':
                    num_start = True
                    negative = True
                elif char.isnumeric():
                    num_start = True
                    num = int(char)
                else:
                    return 0
            else:
                if char.isnumeric():
                    num = num * 10 + int(char)
                    if num >= max_val and negative:
                        return - max_val
                    elif num >= max_val - 1 and not negative:
                        return max_val - 1
                else:
                    return -num if negative else num

        return -num if negative else num


print(Solution().myAtoi("2147483647"))
