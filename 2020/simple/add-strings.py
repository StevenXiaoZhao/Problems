class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num = ''
        count1 = len(num1)
        count2 = len(num2)
        count = min(count1, count2)
        left = 0
        i = 0
        while i < count:
            temp = int(num1[count1 - 1 - i]) + int(num2[count2 - 1 - i]) + left
            num = str(temp % 10) + num
            left = int(temp / 10)
            i += 1

        if count1 < count2:
            while i < count2:
                temp = int(num2[count2 - 1 - i]) + left
                num = str(temp % 10) + num
                left = int(temp / 10)
                i += 1
        elif count2 < count1:
            while i < count1:
                temp = int(num1[count1 - 1 - i]) + left
                num = str(temp % 10) + num
                left = int(temp / 10)
                i += 1

        if left > 0:
            num = str(left) + num

        return num


print(Solution().addStrings('989889', '94'))
