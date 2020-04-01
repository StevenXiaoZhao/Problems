# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        
        [head,left,right] = self.findMidNode(head)
        if(head == None):
            return(None)
        else:
            root = TreeNode(head.val)
            if(left!=None):
                root.left = self.sortedListToBST(left)
            if(right!=None):
                root.right = self.sortedListToBST(right)
            return(root)    
        
    def findMidNode(self, head):
        num = 0
        p = ListNode(0)
        p.next = head
        while(p.next!=None):
            num +=1
            p.next = p.next.next
        if(num == 0):
            return ([None,None,None])
        elif(num ==1):
            return ([head,None,None])
        elif(num == 2):
            p.next = head.next
            head.next = None
            return ([p.next,head, None])
        p.next = head
        for i in range(0, num//2-1):
            p.next = p.next.next
        root = ListNode(0)
        root.next = p.next.next
        p.next.next = None
        q = ListNode(0)
        q.next = root.next.next
        return([root.next,head, q.next])
            
def BuildList(data):
    head = ListNode(data[0])
    p= head
    for i in range(1, len(data)):
        p.next = ListNode(data[i])
        p=p.next
    return(head)
def trasverse(root):
    if(root == None):
        return
    else:
        trasverse(root.left)
        print(root.val)
        trasverse(root.right)
        
testData=[1,2,3,4,5,6,7,8]
ss= Solution()
result = ss.sortedListToBST(BuildList(testData))
trasverse(result)        