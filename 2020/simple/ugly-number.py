class Solution:
    def isUgly(self, num: int) -> bool:
        if num <=0:
            return False
        if num == 1:
            return True
        divide = [1024,729,625, 32, 27, 25, 5, 4, 3, 2]

        for i in range(len(divide)):
            t= divide[i]
            while num >=t and num%t == 0:
                num = int(num/t)
        return num == 1

print(Solution().isUgly(1024*1024*2))