class Solution:
    def countSegments(self, s: str) -> int:
        if s is None or s=='':
            return 0
        is_blank = True
        word_count = 0
        for char in s:
            if is_blank:
                if char != ' ':
                    is_blank = False
                    word_count+=1
            else:
                if char == ' ':
                    is_blank = True

        return word_count

print(Solution().countSegments('     kjdhka      ajndska     ajkndkja     sj'))