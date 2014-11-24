class Solution:
    # Sunday algorithm
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        hay_len = len(haystack)
        needle_len = len(needle)
        if(hay_len < needle_len):
            return(-1)
        
        i= needle_len-1
        while(i<hay_len):
            j = needle_len -1
            k = i
            Found = True
            while(j>=0):
                if(haystack[k] != needle[j]):
                    Found = False
                    break
                j -=1
                k -=1
            if(Found):
                return(i-needle_len+1)
            elif(i == hay_len -1):
                return(-1)
            else:
                k =i+1
                j = needle_len-1
                while(j>=0):
                    if(haystack[k] == needle[j]):
                        break
                    j -=1
                i += needle_len -j
        return(-1)
ss = Solution()
result = ss.strStr('mississippi','a')
print(result)