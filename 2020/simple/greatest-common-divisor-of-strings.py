class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_set = set(str1)
        str2_set = set(str2)
        if str1_set != str2_set:
            return ''

        count = len(str1)
        pattern = ''
        for i in range(count):
            char = str1[i]
            if len(str1_set) >0:
                if char in str1_set:
                    str1_set.remove(char)
            elif char == str1[0]:
                j=1
                while j<i:
                    if i+j<count and str1[j] != str1[i+j]:
                        i+=j
                        break

                if j==i: # maybe pattern found
                    pattern_length = i
                    if len(str1)%pattern_length !=0:
                        i+=i-1
                    else:
                        pattern = str1[0:i]
                        while i<count:
                            for j in range(pattern_length):
                                if pattern[j] != str1[i+j]:
                                    pattern=''
                                    break

                        if j == count:
                            break

        for j in range(len(pattern)):
            if pattern[j] != str1[i + j]:
                pattern = ''
                break

