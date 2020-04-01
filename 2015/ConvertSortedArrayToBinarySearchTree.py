# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        num_len = len(num)
        if(num_len<=0):
        	return None
        return(self.sortedArrayToBSTForSegment(num,0,num_len-1))


    def sortedArrayToBSTForSegment(self, num, start_index, end_index):
    	if(start_index > end_index):
    		return(None)
    	elif(start_index == end_index):
    		return(TreeNode(num[start_index]))
    	else:
    		mid = (start_index + end_index)//2
    		root = TreeNode(num[mid])
    		root.left = self.sortedArrayToBSTForSegment(num, start_index, mid-1)
    		root.right = self.sortedArrayToBSTForSegment(num, mid+1, end_index)
    		return root

ss= Solution()
result = ss.sortedArrayToBST([1,2,3,4,5])
print(result.val)
