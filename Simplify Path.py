class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path == None or path == "":
            return("/")
        stack = []
        symbols = path.split("/")
        for symbol in symbols:
            if symbol == "..":
                if(len(stack) >0):
                    stack.pop()
            elif symbol == "." or symbol == "/" or symbol == "":
                continue
            else:
                stack.append(symbol)
        if len(stack) == 0:
            return("/")
        else:
            result = ""
            for symbol in stack:
                result += "/" + symbol
            return(result)
ss = Solution()
test = "/a/.//b/../../c/"
print(ss.simplifyPath(test))