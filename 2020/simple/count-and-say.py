class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'
        for i in range(n-1):
            num = 0
            curr_char = curr[0]
            new = ''
            for char in curr:
                if char == curr_char:
                    num+=1
                else:

                    new = new + str(num) + curr_char
                    curr_char = char
                    num =1

            curr = new + str(num) + curr_char

        return curr

print(Solution().countAndSay(30))