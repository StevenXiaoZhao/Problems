# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists
    def pathSum(self, root, sum):
        result = self.PathSumWithPrev(root, sum, [])
        if(result == [[]]):
            result = []
        return(result)
        
    def PathSumWithPrev(self, root, sum, prev):
        if(root == None):
            return([[]])
        else:
            leftVal = sum - root.val
            prev.append(root.val)
            if(root.left == None and root.right == None and leftVal == 0):    
                return([prev])
            else:
                left = self.PathSumWithPrev(root.left,leftVal,prev)
                right = self.PathSumWithPrev(root.right,leftVal, list(prev))
                result = []
                if(left != [[]]):
                    result = left
                if(right != [[]]):
                    if(result == []):
                        result = right
                    else:
                        result.extend(right)
                if(result == []):
                    result = [[]]
                return(result)

ss= Solution()
a= TreeNode(1)
a.left = None
a.right = None

b= TreeNode(1)
b.left = None
#b.right = a

c= TreeNode(3)
c.left = b
c.right = a

d= TreeNode(4)
d.left = c

result = ss.pathSum(c,4)
print(result)
        