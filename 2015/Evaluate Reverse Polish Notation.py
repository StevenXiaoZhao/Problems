class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for x in tokens:
            if x == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1+num2
                stack.append(result)
            elif x == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1-num2
                stack.append(result)
            elif x == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1*num2
                stack.append(result)
            elif x == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                result = abs(num1)//abs(num2)
                if(num1*num2<0):
                    result = -result
                stack.append(result)
            else:
                stack.append(int(x))
        return(stack[0])
ss = Solution()
result = ss.evalRPN( 
                ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])
print(result)
        